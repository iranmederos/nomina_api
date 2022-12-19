from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
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
            if user is not None and user.status == True:#user.is_active:
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
        try:
            token_request = request.headers.get('token', None)
            token = Token.objects.get(key=token_request)
            if token: 
                user = CustomUser.objects.filter(auth_token=token).first()
                user.auth_token.delete()
                logout(request)
                return Response({"msg": "Sesion finalizada"},status=status.HTTP_200_OK)
            return Response({"error":"El usuario no existe"}, status=status.HTTP_400_BAD_REQUEST)   
        except:
            return Response({"error":"El usuario no existe"}, status=status.HTTP_400_BAD_REQUEST)   




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

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def disableUser(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user.status = False
        UserSerializer(user, many=False)
        user.save()
        data = {
            "message": "Usuario deshabilitado exitosamente",
        }
        return Response(data, status = 200)
    except:
        return Response({"error": "No existe ningun usuario con ese ID"}, status = 404)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user.identification_card = request.data.get("identification_card", None)
        user.rfc_equivalet = request.data.get("rfc_equivalet", None)
        user.nss = request.data.get("nss", None)
        user.first_name = request.data.get("first_name", None)
        user.last_name = request.data.get("last_name", None)
        user.email = request.data.get("email", None)
        serializer = UserSerializer(user, many=False)
        user.save()
        return Response(serializer.data)
    except:
        return Response({"error": "No existe un usuario con ese id"}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changePassword(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        current_password = request.data.get("current_password", None)
        new_password = request.data.get("new_password", None)
        confirm_password = request.data.get("confirm_password", None)

        if current_password is None or new_password is None or confirm_password is None:
            return Response({"error": "Todos los datos son obligatorios"}, status.HTTP_400_BAD_REQUEST)

        current_password_is_correct=check_password(current_password, user.password)
        if current_password_is_correct:
            if new_password == confirm_password:
                user.password = make_password(new_password)
                user.save()
                serializer = UserSerializer(user, many=False)
                return Response({
                    "user": serializer.data,
                    "msg": "El password ha sido cambiado exitosamente"
                })
            return Response({"error": "Las contraseñas no coinciden"}, status.HTTP_400_BAD_REQUEST)

        return Response({
                "current_password": current_password,
                "user.password": user.password,
                "error": "La contraseña actual es incorrecta"
                }, status.HTTP_400_BAD_REQUEST)
    except: 
        return Response({"error": "No existe un usuario con ese id"}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mensaje(request):
     return Response({"msg":"Hola Mundo"})
