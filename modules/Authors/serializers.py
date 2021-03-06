from rest_framework import serializers
from .models import Author
from modules.Books.serializers import BookSerializer

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ("id","name","last_name","nationality","biography",
        "gender","age","is_alive")





class AuthorBookSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True,many=True)
    class Meta:
        model = Author
        fields = ("id","name","last_name","nationality","biography",
        "gender","age","is_alive","books")