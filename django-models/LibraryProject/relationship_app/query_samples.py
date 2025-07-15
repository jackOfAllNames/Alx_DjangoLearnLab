"""
Sample data creation script for the Library Management System.

This script demonstrates how to create and populate the database with sample data
including authors, books, libraries, and librarians to test the Django models.
"""

from .models import Author, Book, Library, Librarian

# Create sample authors
a1 = Author.objects.create(name="Chimamanda Ngozi Adichie")
a2 = Author.objects.create(name="Chinua Achebe")
a3 = Author.objects.create(name="Wole Soyinka")

# Create sample books and associate them with their respective authors
b1 = Book.objects.create(title="Americanah", author=a1)
b2 = Book.objects.create(title="Things Fall Apart", author=a2)
b3 = Book.objects.create(title="Death and the King's Horseman", author=a3)

# Create sample libraries in different locations
lib1 = Library.objects.create(name="Central Library")
lib2 = Library.objects.create(name="Community Library")
lib3 = Library.objects.create(name="University Library")

# Add books to libraries - demonstrating many-to-many relationships
# Each library can have multiple books, and books can be in multiple libraries
lib1.books.add(b1, b2)
lib2.books.add(b2, b3)
lib3.books.add(b1, b3)

# Create librarians and assign them to their respective libraries
# Demonstrating one-to-one relationships between librarians and libraries
Librarian.objects.create(name="Grace Okoro", library=lib1)
Librarian.objects.create(name="Ahmed Yusuf", library=lib2)
Librarian.objects.create(name="Helen Ade", library=lib3)

# Query all books by a specific author
# Use a join with a double‑underscore lookup
wole_book = Book.objects.filter(author__name="Wole Soyinka")
print(wole_book)

# List all books in a library.
all_books = Library.objects.all()

# Retrieve the librarian for a library.