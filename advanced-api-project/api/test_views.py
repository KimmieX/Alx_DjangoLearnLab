from rest_framework.test import APITestCase
from django.urls import reverse
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
        self.assertIn("title", response.data)
        self.assertEqual(response.data["title"], "New Book")
