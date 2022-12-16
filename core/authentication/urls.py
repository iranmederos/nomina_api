from django.urls import path, include
from .views import mensaje, LoginView, LogoutView, SignUpView, disableUser

urlpatterns = [
    # Auth views
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('disable-user/<int:user_id>/', disableUser),
    path('signup/', SignUpView.as_view()),
    path('users/test/', mensaje),
]