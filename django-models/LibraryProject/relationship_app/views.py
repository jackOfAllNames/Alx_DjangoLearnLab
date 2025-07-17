from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book
from .models import Library
from .forms import RegisterForm

# Create your views here.
def display_books(request):
    # List of books title and author
    all_books = Book.objects.all()
    context = {
        'books': all_books
    }
    return render(request, "relationship_app/list_books.html", context)

def list_books(request):
    libraries = Library.objects.prefetch_related('books')
    return render(request, 'libraries.html', {'libraries': libraries})

def library_details(request, pk):
    library = Library.objects.get(pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    queryset = Library.objects.prefetch_related("books__author")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def home(request):
    return HttpResponse(f"Hello, {request.user.username}!" if request.user.is_authenticated else "Welcome Guest")