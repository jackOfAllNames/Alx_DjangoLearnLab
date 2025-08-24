from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, RegisterView, LoginToken, UnfollowUserView, FollowUserView, FeedView

urlpatterns = [
    path('', HomeView, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginToken.as_view(), name='api_token_auth'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('feed/', FeedView.as_view(), name='feed'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)