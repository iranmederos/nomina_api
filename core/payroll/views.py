# from django.shortcuts import render
from rest_framework.decorators import api_view
# from rest_framework import status
from rest_framework.response import Response
from django.conf import settings

from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
import os
from .models import Payroll, CustomUser
from authentication.serializers import CustomUserSerializer, UserSerializer
from .serializers import PayrollSerializer
from rest_framework import generics

from django.http import HttpResponse


# Create your views here.
@api_view(['POST']) 
def payrolls_register(request):
    s = StaticFilesStorage()
    files = list(get_files(s, location='pdf_files/2022'))
    for file in files:
        pdf_filename = file.split('\\')[1] # "NOM1221_2022-01-01.pdf"
        pdf_dataname = pdf_filename.split('_')
        employee_data = pdf_dataname[0]
        code_employee = employee_data.split('NOM')[1]
        data_pdf = pdf_dataname[1]
        date_pdf = data_pdf.split('.pdf')[0]
            
        user = CustomUser.objects.get(code_employee=code_employee)
        Payroll.objects.create(
            user = user,
            payment_date = date_pdf,
            payroll_filename = pdf_filename
        )

    return Response({
        # "code_employee": code_employee,
        # "user": serializer.data,
        # "user_id": user.id,
        # "date": date_pdf,
        # "pdf_filename": pdf_filename
        "msg": "Registros realizados"
    })


@api_view(['GET'])
def get_payrolls(request):
    payrolls = Payroll.objects.all()
    serializer = PayrollSerializer(payrolls, many=True)
    return Response(serializer.data)
    
 
def download_pdf(request, file_name):
        #s = StaticFilesStorage()
        #file_url = s.url(f'pdf_files/{file_name}')
        file_path = os.path.join(settings.STATIC_ROOT, 'pdf_files', file_name)
        with open(file_path, 'rb') as f:
                file_content = f.read()
        response = HttpResponse(file_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
 
def detail_pdf(request, file_name):
        #s = StaticFilesStorage()
        #file_url = s.url(f'pdf_files/{file_name}')
        file_path = os.path.join(settings.STATIC_ROOT, 'pdf_files', file_name)
        with open(file_path, 'rb') as f:
                file_content = f.read()
        response = HttpResponse(file_content, content_type='application/pdf')
        #response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response