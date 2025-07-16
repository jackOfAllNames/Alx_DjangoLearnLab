from django.contrib import admin
from django.urls import path
from .views import display_books, library_details
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('books/', display_books),
    path('libraries/', list_books),
    # path('library/<int:pk>', library_details)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]
