from django.urls import path, include
from .views import HomeView, SignUpView, LogInView, LogOutView, ProfileView
from .views import PostCreateView, ListPostsView, DeletePostView, DetailPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', ProfileView, name='profile'),

    path('posts/', ListPostsView.as_view(), name='posts'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
    path('posts/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
]
