from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'code_employee', 'identification_card', 'rfc_equivalet', 'nss', 'first_name', 'last_name', 'email', 'status', 'date_start', 'rol', 'password']


class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = CustomUser
         fields = "__all__"