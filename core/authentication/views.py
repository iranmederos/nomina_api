from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer
from .messages.responses_ok import LOGIN_OK, SIGNUP_OK
from .messages.responses_error import LOGIN_CREDENTIALS_REQUIRED_ERROR 

# Create your views here.
class LoginView(APIView):
    def get(self, request):
        data_response = {"msg": "Método GET no permitido"}
        return Response(data_response, status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        user = request.data.get('username', None)
        password = request.data.get('password', None)
       
        if user is None or password is None:
            return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = authenticate(user = user, password = password)
            if user is not None:
                return Response( {
                "user": UserSerializer(user, context = self.get_serializer_context()).data,
                "message": LOGIN_OK
            }, status=status.HTTP_200_OK)
            else:
                return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        # Borramos de la request la información de sesión
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)