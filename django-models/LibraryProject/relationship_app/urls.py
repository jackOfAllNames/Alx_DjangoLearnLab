from django.contrib import admin
from django.urls import path
from .views import display_books, library_details
from .views import list_books, CustomLoginView, CustomLogoutView, register_view
from .views import LibraryDetailView

urlpatterns = [
    path('books/', display_books),
    path('libraries/', list_books),
    # path('library/<int:pk>', library_details)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
]
