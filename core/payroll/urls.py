from django.urls import path
from .views import payrolls_register

urlpatterns = [
    # Payroll views
    path('payroll-register/', payrolls_register),
]