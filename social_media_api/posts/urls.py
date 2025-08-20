from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostAPIView

router = DefaultRouter()
router.register(r'posts', PostAPIView, basename='post')

urlpatterns = [
    path('api/', include(router.urls)),
]
