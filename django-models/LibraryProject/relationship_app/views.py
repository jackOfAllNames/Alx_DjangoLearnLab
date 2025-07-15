from django.shortcuts import render
from .models import Book

# Create your views here.
def display_books(request):
    # List of books title and author
    all_books = Book.objects.all()
    context = {
        'books': all_books
    }
    return render(request, "relationship_app/list_books.html", context)
