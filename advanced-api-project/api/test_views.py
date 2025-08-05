from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User
from .views import ListView, CreateView, UpdateView, DeleteView, DetailView


class BookTestCases(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='olaitan', password='Vnp-1234')
        Author.objects.create(name="Chinua Achebe")
        Author.objects.create(name="Wole Soyinka")
        Author.objects.create(name="Chimamanda Ngozi Adichie")
        Book.objects.create(title="A Man of the People", publication_year=1966, author_id=1)
        Book.objects.create(title="Death and the King's Horseman", publication_year=1975, author_id=2)
        # Book.objects.create(title="Purple Hibiscus", publication_year=2003, author_id=3)
        Book.objects.create(title="Half of a Yellow Sun", publication_year=2006, author_id=3)

    def test_list_books(self):
        request = self.factory.get('books/')
        force_authenticate(request, user=self.user)

        view = ListView.as_view()
        view.cls.permission_classes = [IsAuthenticated]
        response = view(request)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[1]['title'], "Death and the King's Horseman")

    def test_create_book(self):
        request = self.factory.post('books/create/', {"title": "Purple Hibiscus", "publication_year" : 2003, "author" : 3}, format="json")
        view = CreateView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['publication_year'], 2003)
    
    def test_get_book_details(self):
        request = self.factory.get('books/<int:pk>/')
        view = DetailView.as_view()
        response = view(request, pk=3)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['publication_year'], 2006)
    
    def test_no_book_details(self):
        request = self.factory.get('books/<int:pk>/')
        view = DetailView.as_view()
        response = view(request, pk=5)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_book(self):
        request = self.factory.put('books/update/<int:pk>/', {"title": "Purple Hibiscus", "publication_year" : 2001, "author" : 3}, format="json")
        view = UpdateView.as_view()
        response = view(request, pk=3)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['author'], 3)

    def test_delete_book(self):
        book = Book.objects.create(title="Purple Hibiscus", publication_year=2003, author_id=3)

        request = self.factory.delete('books/delete/<int:pk>/')
        view = DeleteView.as_view()
        response = view(request, pk=book.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)