from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notice_board.views import (AdCreateAPIView, AdDestroyAPIView,
                                AdListAPIView, AdRetrieveAPIView,
                                AdUpdateAPIView, CommentViewSet)
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('create/', AdCreateAPIView.as_view(), name='ad-create'),
    path('', AdListAPIView.as_view(), name='ads-list'),
    path('<int:pk>/', AdRetrieveAPIView.as_view(), name='ad-retrieve'),
    path('<int:pk>/update/', AdUpdateAPIView.as_view(), name='ad-update'),
    path('<int:pk>/delete/', AdDestroyAPIView.as_view(), name='ad-delete'),
    path('<int:pk>/', include(router.urls)),
]
