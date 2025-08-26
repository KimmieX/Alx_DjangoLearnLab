from rest_framework import serializers
from .models import Book  # Make sure Book model is defined in models.py

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Includes all fields from the Book model