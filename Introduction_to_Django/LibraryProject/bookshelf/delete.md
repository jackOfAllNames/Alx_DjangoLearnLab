# Create a Book instance

This shows how the book is created in the Django shell.

## Command
```python
>>> book = Book.objects.get(title="1984")
>>> book.delete()
>>> Book.objects.all()
```

## Output
```bash
<QuerySet []>
```
