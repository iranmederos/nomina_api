from django.urls import path, include
from .views import mensaje, LoginView, LogoutView, SignUpView

urlpatterns = [
    # Auth views
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('signup/', SignUpView.as_view()),
    path('users/test/', mensaje),
]