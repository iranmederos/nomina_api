from django.urls import path, include
from .views import mensaje, LoginView, LogoutView, SignUpView, disableUser, getUsers, updateUser, changePassword, send_mail_message

urlpatterns = [
    # Auth views
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('disable-user/<int:user_id>/', disableUser),
    path('signup/', SignUpView.as_view()),
    path('get-users/', getUsers),
    path('update-user/<int:user_id>/', updateUser),
    path('change-password/<int:user_id>/', changePassword),
    path('send-mail-message/', send_mail_message),

    path('users/test/', mensaje),
]