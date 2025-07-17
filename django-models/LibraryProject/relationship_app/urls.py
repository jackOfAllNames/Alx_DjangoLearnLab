from django.contrib import admin
from django.urls import path
from .views import display_books, library_details, register, home
from .views import list_books, CustomLoginView, CustomLogoutView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import LibraryDetailView

urlpatterns = [
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
    path('books/', display_books),
    path('libraries/', list_books),
    # path('library/<int:pk>', library_details)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('books/', views.book_list, name='book_list'),
    path('', home, name='home'),
]
