from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import render, HttpResponse
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

def index(request):
    return HttpResponse("Hello, world! This is the API index page.")

class ListAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filterset_fields = ['publication_year', 'title', 'author']
    search_fields = ['title']

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
