from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostAPIView, CommentAPIView, FeedView

router = DefaultRouter()
router.register(r'posts', PostAPIView, basename='post')
router.register(r'comments', CommentAPIView, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
]
