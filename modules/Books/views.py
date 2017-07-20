
from .models import Book
from rest_framework import generics
from .serializers import *
# Create your views here.

class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = BookSerializer
     queryset = Book.objects.all()

class BookAuthorList(generics.ListAPIView):
     serializer_class = BookAuthorSerializer
     queryset = Book.objects.all()
