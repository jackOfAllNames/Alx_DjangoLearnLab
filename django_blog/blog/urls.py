from django.urls import path, include
from .views import HomeView, SignUpView, LogInView, LogOutView, ProfileUpdateView, ProfileView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('posts/', LogOutView.as_view(), name='posts'),
    # path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('profile/', ProfileView, name='profile'),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/register/', SignUpView.as_view(), name='signup'),
    # path('posts/', name='posts'),
    # path('profile/', name='profile'),
]
