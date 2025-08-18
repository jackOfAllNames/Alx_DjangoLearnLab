from django.urls import path
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)