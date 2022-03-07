from rest_framework import serializers
from books_api.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'subtitle', 'author', 'ISBN',)