from django.urls import path
from .views import index
from .views import ListAuthors

urlpatterns = [
    path('', index),
    path('authors/', ListAuthors.as_view(), name='list-authors'),
]
