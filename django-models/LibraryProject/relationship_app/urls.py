from django.contrib import admin
from django.urls import path
from .views import display_books

urlpatterns = [
    path('', display_books),
]
