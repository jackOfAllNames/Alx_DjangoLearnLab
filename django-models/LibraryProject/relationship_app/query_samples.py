from .models import Author, Book, Library, Librarian

a1 = Author.objects.create(name="Chimamanda Ngozi Adichie")
a2 = Author.objects.create(name="Chinua Achebe")
a3 = Author.objects.create(name="Wole Soyinka")