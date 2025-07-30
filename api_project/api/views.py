from django.shortcuts import render, HttpResponse
from .serializers import BookSerializer
from rest_framework import generics
from .models import Book

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!')

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer