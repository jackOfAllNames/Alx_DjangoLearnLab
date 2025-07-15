from django.contrib import admin
from django.urls import path
from .views import display_books, libraries_list, library_details

urlpatterns = [
    path('books/', display_books),
    path('libraries/', libraries_list),
    path('library/<int:pk>', library_details)
]
