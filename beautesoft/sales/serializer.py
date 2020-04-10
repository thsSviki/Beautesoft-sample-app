from rest_framework import serializers
from .models import Custom

class UserSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    email=serializers.EmailField(max_length=100)
    password=serializers.CharField(max_length=100)