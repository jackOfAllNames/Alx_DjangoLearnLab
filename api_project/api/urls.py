from django.contrib import admin
from django.urls import path, include
from .views import index, BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')

urlpatterns = [
    path('', index),
    path('views/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
