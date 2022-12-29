from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Payroll(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING) 
    payment_date = models.DateField(null=False, blank=False)
    payroll_filename = models.CharField(max_length=100, unique=True, null=False, blank=True)

    def __str__(self):
        return f"{self.user} - {self.payment_date}"