from django.urls import path, include
from .views import mensaje, Login, Logout
# from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # Auth views
    # path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('login/', Login.as_view(), name='auth_login'),
    # path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout/', Logout.as_view(), name='auth_logout'),


    #  path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

     path('users/test/', mensaje),
]