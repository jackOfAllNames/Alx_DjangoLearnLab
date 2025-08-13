from django.urls import path, include
from .views import HomeView, SignUpView, LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', SignUpView.as_view(), name='signup'),
]
