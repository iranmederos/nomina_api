'''
Modelo CustomUser personalizado a partir del modelo User
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser, Roles

# Register your models here.
class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ('id', 'code_employee', 'identification_card', 'rfc_equivalet', 'nss', 'first_name', 'last_name', 'email', 'status', 'date_start', 'rol', 'password')
        
admin.site.register(CustomUser, CustomUserAdmin) #CustomUser es un modelo y CustomUserAdmin es la vista a mostrar del modelo 
admin.site.register(Roles)
admin.site.unregister(Group)

