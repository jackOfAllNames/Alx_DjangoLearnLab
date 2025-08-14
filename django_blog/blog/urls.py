from django.urls import path, include
from .views import HomeView, SignUpView, LogInView, LogOutView, ProfileView
from .views import PostCreateView, ListPostsView, DeletePostView, DetailPostView, UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView, name='profile'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),

    # Post-related URLs
    path('posts/', ListPostsView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
]
