from django.shortcuts import render

# Create your views here.

from .models import Books, Author, Category
from rest_framework import permissions, viewsets
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer

class BookViewSet(viewsets.ModelViewSet):

    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Change to IsAuthenticated when submitted



class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]



class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]
