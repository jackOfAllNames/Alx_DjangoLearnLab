from django.urls import path, include
from .views import HomeView, SignUpView, LogInView, LogOutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/register/', SignUpView.as_view(), name='signup'),
    # path('posts/', name='posts'),
    # path('profile/', name='profile'),
]
