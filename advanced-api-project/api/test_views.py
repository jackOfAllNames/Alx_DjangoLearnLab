from rest_framework.test import APIRequestFactory
from django.test import TestCase
from .models import Author, Book
from .views import ListView, CreateView


class BookTestCases(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        Author.objects.create(name="Chinua Achebe")
        Author.objects.create(name="Wole Soyinka")
        Author.objects.create(name="Chimamanda Ngozi Adichie")
        Book.objects.create(title="A Man of the People", publication_year=1966, author_id=1)
        Book.objects.create(title="Death and the King's Horseman", publication_year=1975, author_id=2)
        # Book.objects.create(title="Purple Hibiscus", publication_year=2003, author_id=3)
        Book.objects.create(title="Half of a Yellow Sun", publication_year=2006, author_id=3)

    def test_list_books(self):
        request = self.factory.get('books/')
        view = ListView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[1]['title'], "Death and the King's Horseman")

    def test_create_book(self):
        request = self.factory.post('books/create/', {"title": "Purple Hibiscus", "publication_year" : 2003, "author" : 3}, format="json")
        view = CreateView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['publication_year'], 2003)

