# from django.shortcuts import render
# from django.contrib.auth import authenticate
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import CustomUser

# from .serializers import UserSerializer, RegisterSerializer
# from .messages.responses_ok import LOGIN_OK, SIGNUP_OK
# from .messages.responses_error import LOGIN_CREDENTIALS_REQUIRED_ERROR, LOGIN_CREDENTIALS_ERROR

# # Create your views here.
# class LoginView(generics.GenericAPIView):
#     def get(self, request):
#         data_response = {"msg": "Método GET no permitido"}
#         return Response(data_response, status.HTTP_405_METHOD_NOT_ALLOWED)

#     def post(self, request):
#         email = request.data.get("email", None)
#         password = request.data.get("password", None)

#         if email is None or password is None:
#             return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             user = authenticate(email = email, password = password)
#             if user is not None:
#                 return Response( {
#                 "user": UserSerializer(user, context = self.get_serializer_context()).data,
#                 "message": LOGIN_OK
#             }, status=status.HTTP_200_OK)
#             else:
#                 return Response(LOGIN_CREDENTIALS_ERROR, status=status.HTTP_401_UNAUTHORIZED)

# class SignUpView(generics.GenericAPIView):

#     serializer_class = RegisterSerializer
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)#retorna el serializer_class definido previamente
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response(
#             {
#                 "user": UserSerializer(user, context = self.get_serializer_context()).data,
#                 "message": SIGNUP_OK
#             },
#         )


# @api_view(['GET'])
# def getAllUsers(request):
#     users = CustomUser.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getUserById(request, user_id):
#     try:
#         user = CustomUser.objects.get(id=user_id)
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status = 200)
#     except:
#         return Response({"msg": "No existe ningun usuario con ese ID"}, status = 404)

# @api_view(['PUT'])
# def updateUser(request, user_id):
#     try:
#         data = request.data
#         user = CustomUser.objects.get(id=user_id)
#         serializer = UserSerializer(instance=user, data=data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     except:
#         return Response({"msg": "No existe ningun usuario con ese ID"}, status = 404)
        
# @api_view(['DELETE'])
# def deleteUser(request, user_id):
#     try:
#         user = CustomUser.objects.get(id=user_id)
#         user.delete()
#         data = {
#             "message": "Usuario eliminado exitosamente"
#         }
#         return Response(data, status = 200)
#     except:
#         return Response({"msg": "No existe ningun usuario con ese ID"}, status = 404)
