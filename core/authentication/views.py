from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer, CustomUserSerializer, RegisterSerializer
from .messages.responses_ok import LOGIN_OK, SIGNUP_OK
from .messages.responses_error import LOGIN_CREDENTIALS_REQUIRED_ERROR, LOGIN_CREDENTIALS_ERROR

# Create your views here.
class LoginView(GenericAPIView):
    def get(self, request):
        data_response = {"msg": "Método GET no permitido"}
        return Response(data_response, status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        code_employee = request.data.get("code_employee", None)
        password = request.data.get("password", None)

        if code_employee is None or password is None:
            return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST)
        else: 
            user = authenticate(code_employee = code_employee, password = password)
            if user is not None and user.is_active:
                token = Token.objects.get_or_create(user=user)
                if token:
                    return Response( {
                        "token": token[0].key,
                        "user": CustomUserSerializer(user, context = self.get_serializer_context()).data,
                        "message": LOGIN_OK
                    }, status=status.HTTP_200_OK)
                token.delete()
                token = Token.objects.create(user=user)
                return Response( {
                    "token": token[0].key,
                    "user": CustomUserSerializer(user, context = self.get_serializer_context()).data,
                    "message": LOGIN_OK
                }, status=status.HTTP_200_OK)
 
            else:
                return Response(LOGIN_CREDENTIALS_ERROR, status=status.HTTP_401_UNAUTHORIZED)

# @permission_classes([IsAuthenticated])
class LogoutView(GenericAPIView):
    def post(self, request):
            token_request = request.headers.get('token', None)
            token = Token.objects.filter(key=token_request).first()
            if token: 
                user = CustomUser.objects.filter(auth_token=token).first()
                user.auth_token.delete()
                logout(request)
                return Response({"msg": "Sesion finalizada"},status=status.HTTP_200_OK)
            return Response({"Error":"Ocurrio un error"}, status=status.HTTP_400_BAD_REQUEST)      



class SignUpView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context = self.get_serializer_context()).data,
                "message": SIGNUP_OK
            },
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mensaje(request):
     return Response({"msg":"Hola Mundo"})