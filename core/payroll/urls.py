from django.urls import path
from .views import payrolls_register, get_payrolls, download_pdf, detail_pdf

urlpatterns = [
    # Payroll views
    path('payroll-register/', payrolls_register),
    path('get-payrolls/', get_payrolls),
    path('download/<str:file_name>/', download_pdf, name='download_pdf'),
    path('detail_pdf/<str:file_name>/', detail_pdf, name='detail_pdf'),
]