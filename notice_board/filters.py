import django_filters

from notice_board.models import Ad


class AdFilter(django_filters.rest_framework.FilterSet):
    """
    Фильтр для модели Ad, позволяющий фильтровать объявления по названию.

    Атрибуты:
        title (django_filters.CharFilter): Фильтр для поля 'title' модели Ad.
            Позволяет искать объявления, название которых содержит указанный текст.
            Поиск производится без учета регистра.

    Метакласс Meta:
        model (Model): Модель, к которой применяется фильтр.
        fields (tuple): Поля модели, по которым можно фильтровать объявления.
    """
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
    )

    class Meta:
        model = Ad
        fields = ('title',)
