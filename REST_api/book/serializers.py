from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    pass
    # class Meta:
    #     model = Book
    #     fields = '__all__'
    #     #fields = ('isbn', 'title')
