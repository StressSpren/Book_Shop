from .models import Books, Author, Category
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Books
        fields = [
           'id', 'url', 'title', 'author',
            'description', 'cover_image', 
            'price', 'stock', 'published_date', 'isbn', 'category']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields =[
            'first_name', 'last_name', 'bio', 'profile_picture',
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [

            'name'
    ]