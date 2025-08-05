from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, HttpResponse
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book

def index(request):
    return HttpResponse("Hello, world! This is the API index page.")

class ListAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        publication_year_params = self.request.query_params.get('publication_year', None)
        if publication_year_params:
            queryset = queryset.filter(publication_year=publication_year_params)
        return queryset

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
