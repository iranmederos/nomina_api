from django.urls import path
from .views import payrolls_register, get_payrolls, download_payroll, detail_payroll

urlpatterns = [
    # Payroll views
    path('payroll-register/', payrolls_register),
    path('get-payrolls/', get_payrolls),
    path('download_payroll/', download_payroll, name='download_payroll'),
    path('detail_payroll/', detail_payroll, name='detail_payroll'),
    # path('detail_pdf/<str:file_name>/', detail_pdf, name='detail_pdf'),
]