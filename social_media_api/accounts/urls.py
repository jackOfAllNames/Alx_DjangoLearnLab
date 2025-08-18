from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, RegisterView, LoginToken

urlpatterns = [
    path('', HomeView, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginToken.as_view(), name='api_token_auth'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)