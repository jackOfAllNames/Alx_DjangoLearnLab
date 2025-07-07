# Delete the Book instance

This removes the book and shows the table is empty.

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
