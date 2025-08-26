from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

author = Author.objects.get(name="Chimamanda Ngozi Adichie")
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(book.title)

library = Library.objects.get(name="Accra Central Library")
librarian = Librarian.objects.get(library=library)

print(librarian.name)



