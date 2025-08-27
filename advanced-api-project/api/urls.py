from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete')

]