from dataclasses import field
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        filed = [' email ',' password' , 'is_verified']


    class VerifyAccountsSerializer(serializers.Serializer):
        email = serializers.EmailFields()


    class LoginSerializer(serializers.Serializer):
        email = serializers.EmailField
        password = serializers.Charfield()