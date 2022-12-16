from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'code_employee', 'identification_card', 'rfc_equivalet', 'nss', 'first_name', 'last_name', 'email', 'status', 'date_start', 'rol')


class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = CustomUser
         fields = "__all__"


# class UserTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'code_employee', 'identification_card', 'rfc_equivalet', 'nss', 'first_name', 'last_name', 'email', 'status', 'date_start', 'rol')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'code_employee', 'identification_card', 'rfc_equivalet', 'nss', 'first_name', 'last_name', 'email', 'status', 'date_start', 'rol', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['code_employee'],
            code_employee = validated_data['code_employee'],
            identification_card = validated_data['identification_card'],
            rfc_equivalet = validated_data['rfc_equivalet'],
            nss = validated_data['nss'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            password = validated_data['password'])
        return user