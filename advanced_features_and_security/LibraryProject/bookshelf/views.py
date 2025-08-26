# LibraryProject/bookshelf/views.py

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book


def search_books(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        title = form.cleaned_data['title']
        results = Book.objects.filter(title__icontains=title)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'results': results})


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})