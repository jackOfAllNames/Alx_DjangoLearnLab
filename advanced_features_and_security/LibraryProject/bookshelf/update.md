# Update the Book title

This changes the title and saves it.

## Command
```python
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
```

## Output
```bash
```
