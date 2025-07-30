from django.contrib import admin
from django.urls import path
from .views import index, BookList

urlpatterns = [
    path('', index),
    path('views/', BookList.as_view(), name='book-list'),
]
