from django.urls import path
from .views import payrolls_register, get_payrolls

urlpatterns = [
    # Payroll views
    path('payroll-register/', payrolls_register),
    path('get-payrolls/', get_payrolls),
]