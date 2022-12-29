from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Roles(models.Model):
    rol_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}-{self.rol_name}"

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    code_employee = models.IntegerField(unique=True, null=False, blank=False)
    identification_card = models.CharField(max_length=20, unique=True, null=False, blank=False)
    rfc_equivalet = models.CharField(max_length=16, unique=True, null=False, blank=False)
    nss = models.CharField(max_length=20, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    date_start = models.DateField(null=True, blank=True)
    rol = models.ForeignKey(Roles, on_delete=models.DO_NOTHING, null=True, blank=True) 

    USERNAME_FIELD ='code_employee'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return f"{self.get_full_name()}-{self.code_employee}"


