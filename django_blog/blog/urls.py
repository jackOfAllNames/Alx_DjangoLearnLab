from django.urls import path, include
from .views import HomeView, SignUpView, LogInView, LogOutView, ProfileView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView, CommentListView
from .views import PostCreateView, ListPostsView, DeletePostView, DetailPostView, UpdatePostView, PostByTagListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/', ProfileView, name='profile'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),

    # Post-related URLs
    path('posts/', ListPostsView.as_view(), name='posts'),
    path('search/', ListPostsView.as_view(), name='post_search'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post_delete'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),

    # Comment-related URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='create_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comments/', CommentListView.as_view(), name='comments'),
]
