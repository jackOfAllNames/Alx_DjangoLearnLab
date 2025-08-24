from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostAPIView, CommentAPIView, FeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostAPIView, basename='post')
router.register(r'comments', CommentAPIView, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path("<int:pk>/like/", LikePostView.as_view(), name="like-post"),
    path("<int:pk>/unlike/", UnlikePostView.as_view(), name="unlike-post"),
]
