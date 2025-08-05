from rest_framework import generics
from django.shortcuts import render, HttpResponse
from .serializers import AuthorSerializer
from .models import Author, Book

def index(request):
    return HttpResponse("Hello, world! This is the API index page.")

class ListAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
