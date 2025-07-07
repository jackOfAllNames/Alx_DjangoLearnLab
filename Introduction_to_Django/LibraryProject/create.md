# Create a Book instance

This shows how the book is created in the Django shell.

## Command
```python
>>> from bookshelf.models import Book
>>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
