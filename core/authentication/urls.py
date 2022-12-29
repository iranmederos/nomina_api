from django.urls import path, include
from .views import LoginView, LogoutView, SignUpView, disable_user, get_users, update_user, change_password, recovery_password, enable_user, create_role, get_roles

urlpatterns = [
    # Auth views
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('disable-user/<int:user_id>/', disable_user),
    path('signup/', SignUpView.as_view()),
    path('get-users/', get_users),
    path('update-user/<int:user_id>/', update_user),
    path('change-password/<int:user_id>/', change_password),
    path('recovery-password/', recovery_password),
    #Auxiliar URLs
    path('enable-user/<int:user_id>/', enable_user),
    path('create-role/', create_role),
    path('get-roles/', get_roles),
]