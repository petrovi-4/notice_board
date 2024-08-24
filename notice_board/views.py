from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from notice_board.filters import AdFilter
from notice_board.models import Ad, Comment
from notice_board.paginator import AdPaginator
from notice_board.permissions import IsAuthor, IsAdmin
from notice_board.serializers import AdDetailSerializer, AdSerializer, CommentSerializer


class AdCreateAPIView(generics.CreateAPIView):
    """
    Эндпоинт для создания объявлений.

    Этот класс предоставляет метод для создания нового объявления.
    Только аутентифицированные пользователи могут использовать этот эндпоинт.
    """
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Сохраняет новое объявление, присваивая текущего пользователя в качестве автора.

        Параметры:
            serializer (Serializer): Сериализатор, используемый для создания объявления.
        """
        new_ad = serializer.save()
        new_ad.author = self.request.user
        new_ad.save()


class AdListAPIView(generics.ListAPIView):
    """
    Эндпоинт для просмотра списка объявлений.

    Этот класс предоставляет метод для получения списка всех объявлений с возможностью фильтрации.
    Объявления выводятся с пагинацией.
    """
    serializer_class = AdSerializer
    pagination_clas = AdPaginator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def get_queryset(self):
        """
        Возвращает отсортированный по дате создания список объявлений.

        Возврат:
            queryset (QuerySet): Список объявлений, отсортированных по убыванию даты создания.
        """
        queryset = Ad.objects.all().order_by('-created_at')
        return queryset


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """
    Эндпоинт для просмотра конкретного объявления.

    Этот класс предоставляет метод для получения подробной информации о конкретном объявлении.
    Только аутентифицированные пользователи могут использовать этот эндпоинт.
    """
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]


class AdUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования объявления"""
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor or IsAdmin]


class AdDestroyAPIView(generics.DestroyAPIView):
    """
    Эндпоинт для удаления объявления.

    Этот класс предоставляет метод для удаления объявления.
    Только автор объявления или администратор могут использовать этот эндпоинт.
    """
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor or IsAdmin]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для управления комментариями к объявлениям.

    Этот класс предоставляет методы для создания, просмотра, обновления и удаления комментариев.
    Права доступа зависят от действия (создание, просмотр, обновление, удаление).
    """
    serializer_class = CommentSerializer

    def get_queryset(self, *args, **kwargs):
        """
        Возвращает список комментариев, связанных с конкретным объявлением.

        Параметры:
            *args: Дополнительные позиционные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Возврат:
            queryset (QuerySet): Список комментариев, связанных с объявлением.
        """
        ad_pk = self.kwargs.get('pk')
        print(ad_pk)
        queryset = Comment.objects.filter(ad=ad_pk)
        return queryset

    def perform_create(self, serializer, *args, **kwargs):
        """
        Создает новый комментарий, связывая его с объявлением и текущим пользователем.

        Параметры:
            serializer (Serializer): Сериализатор, используемый для создания комментария.
            *args: Дополнительные позиционные аргументы.
            **kwargs: Дополнительные именованные аргументы.
        """
        new_comment = serializer.save()
        new_comment.author = self.request.user
        ad_pk = self.kwargs.get('pk')
        new_comment.ad = Ad.objects.get(pk=ad_pk)
        new_comment.save()

    def get_permissions(self):
        """
        Определяет права доступа в зависимости от выполняемого действия.

        Возврат:
            list: Список экземпляров классов разрешений, применяемых к текущему действию.
        """
        if self.action == 'create' or self.action == 'list' or \
                self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        elif self.action == 'update' or self.action == 'destroy' or \
                self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsAdmin | IsAuthor]
        return [permission() for permission in permission_classes]
