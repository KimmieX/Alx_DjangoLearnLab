from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass123')
        self.client.login(username='tester', password='pass123')
        self.book = Book.objects.create(title="Test Book", author="Author", published_date="2023-01-01")

    def test_create_book(self):
        url = reverse('book-list')  # Adjust to your actual route name
        data = {
            "title": "New Book",
            "author": "New Author",
            "published_date": "2023-05-01"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {"title": "Updated Title"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Title")

    def test_search_books(self):
        url = reverse('book-list') + '?search=Test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

def test_ordering_books(self):
    url = reverse('book-list') + '?ordering=title'
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_permission_denied(self):
        self.client.logout()
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # or 401 depending on setup

# Create your tests here.
