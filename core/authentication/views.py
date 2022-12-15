from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import UserSerializer
from .messages.responses_ok import LOGIN_OK, SIGNUP_OK
from .messages.responses_error import LOGIN_CREDENTIALS_REQUIRED_ERROR 

# Create your views here.
class LoginView(generics.GenericAPIView):
    def get(self, request):
        data_response = {"msg": "Método GET no permitido"}
        return Response(data_response, status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        email = request.data.get("username", None)
        password = request.data.get("password", None)

        if email is None or password is None:
            return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = authenticate(email = email, password = password)
            if user is not None:
                return Response( {
                "user": UserSerializer(user, context = self.get_serializer_context()).data,
                "message": LOGIN_OK
            }, status=status.HTTP_200_OK)
            else:
                return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_401_UNAUTHORIZED)