from django.urls import path
from .views import index
from .views import ListAuthors, ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('', index),
    path('authors/', ListAuthors.as_view(), name='list-authors'),
    path('books/', ListView.as_view(), name='list-books'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='create-book'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='update-book'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='delete-book'),
]
