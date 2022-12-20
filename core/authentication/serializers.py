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
        #tomar del modelo roles el campo de usuario comun
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


class UserSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'identification_card', 'rfc_equivalet', 'nss', 'first_name', 'last_name', 'email']


# class UpdateSerializer(serializers.ModelSerializer):
#     # nss = serializers.CharField(max_length=20, unique=True, null=False, allow_blank=False)
#     class Meta:
#         model = CustomUser
#         fields = ('identification_card', 'rfc_equivalet', 'nss', 'first_name', 'last_name', 'email')#, 'rol')


    # def validate_nss(self, value):
    #     if value == '':
    #         raise serializers.ValidationError('El nss es obligatorio')
    
    # def validate(self, data):
    #     if data['nss']:
    #         return data
    #     raise serializers.ValidationError("el nss es obligatorio")

    # def update(self, instance, validated_data):
    #     instance.identification_card = validated_data.get('name', instance.identification_card)
    #     instance.rfc_equivalet = validated_data.get('rfc_equivalet', instance.rfc_equivalet)
    #     instance.nss = validated_data.get('nss', instance.nss)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance

