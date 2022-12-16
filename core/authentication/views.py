from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
from .models import CustomUser

from .serializers import UserSerializer
from .messages.responses_ok import LOGIN_OK, SIGNUP_OK
from .messages.responses_error import LOGIN_CREDENTIALS_REQUIRED_ERROR 


# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomTokenObtainPairSerializer, CustomUserSerializer



# Create your views here.
# class LoginView(APIView):
#     def get(self, request):
#         data_response = {"msg": "Método GET no permitido"}
#         return Response(data_response, status.HTTP_405_METHOD_NOT_ALLOWED)

#     def post(self, request):
#         # Recuperamos las credenciales y autenticamos al usuario
#         user = request.data.get('username', None)
#         password = request.data.get('password', None)
       
#         if user is None or password is None:
#             return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             user = authenticate(user = user, password = password)
#             if user is not None:
#                 return Response( {
#                 # "user": UserSerializer(user, context = self.get_serializer_context()).data,
#                 "user": UserSerializer(user).data,
#                 "message": LOGIN_OK
#             }, status=status.HTTP_200_OK)
#             else:
#                 return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_401_UNAUTHORIZED)


# class LogoutView(APIView):
#     def post(self, request):
#         # Borramos de la request la información de sesión
#         logout(request)

#         # Devolvemos la respuesta al cliente
#         return Response(status=status.HTTP_200_OK)

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # username = request.data.get('username', '')
        username = request.data.get('code_employee', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de Sesion Existoso'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente.'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe este usuario.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def mensaje(request):
     return Response({"msg":"Hola Mundo"})