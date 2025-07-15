from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Create your views here.
def display_books(request):
    # List of books title and author
    all_books = Book.objects.all()
    context = {
        'books': all_books
    }
    return render(request, "relationship_app/list_books.html", context)

def libraries_list(request):
    libraries = Library.objects.prefetch_related('books')
    return render(request, 'libraries.html', {'libraries': libraries})

def library_details(request, pk):
    library = Library.objects.get(pk=pk)
    return render(request, 'library_detail.html', {'library': library})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    queryset = Library.objects.prefetch_related("books__author")
