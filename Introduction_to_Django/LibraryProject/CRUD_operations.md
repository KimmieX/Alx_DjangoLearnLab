//create Operation
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
//expected output
<Book: 1984 by George Orwell (1949)>

//retrieve operation
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
//expected output
('1984', 'George Orwell', 1949)

//update operation
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
//expected output
'Nineteen Eighty-Four'

//delete operation
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
//expected output
<QuerySet []>