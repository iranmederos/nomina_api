from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
import os
from .models import Payroll, CustomUser
from authentication.serializers import CustomUserSerializer, UserSerializer
from .serializers import PayrollSerializer
from rest_framework.authtoken.models import Token
from django.http import HttpResponse


# Create your views here.
@api_view(['POST']) 
# @permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def get_payrolls(request):
    token_request = request.headers.get("token", None)
    if token_request is not None:
        # token = Token.objects.get(key=token_request)
        token = Token.objects.filter(key=token_request).first()
        if token:
            log_user = CustomUser.objects.filter(auth_token=token).first()
            year = request.data.get("year", None)
            month = request.data.get("month", None)

            if year is None and month is None:
                return Response({"error":"Se requiere mes y/o año"}, status=400)
            
            if year is not None and month is not None:
                    payrolls = Payroll.objects.filter(payment_date__year=year, payment_date__month=month, user=log_user.id)
                    serializer = PayrollSerializer(payrolls, many=True)
                    return Response({"payroll": serializer.data, "year": year, "month": month})
            
            if year is not None and month is None:
                payrolls = Payroll.objects.filter(payment_date__year=year, user=log_user.id)
                serializer = PayrollSerializer(payrolls, many=True)
                return Response({"payroll": serializer.data, "year": year})

            if year is None and month is not None:
                    payrolls = Payroll.objects.filter(payment_date__month=month, user=log_user.id)
                    serializer = PayrollSerializer(payrolls, many=True)
                    return Response({"payroll": serializer.data, "month": month})

        return Response({"error":"Token inexistente"}, status=400)   
    return Response({"error":"Token no encontrado"}, status=400)   
             

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def download_payroll(request):
    file_name = request.data.get('payroll_filename', None)
    # date_pdf = file_name.split('_')[1].split('.pdf')[0]
    # year_folder = date_pdf.split('-')[0]
    
    path = os.path.join(settings.STATIC_ROOT, 'pdf_files')
    for directory_name, directory, files in os.walk(path):
        # directory_name = directory_name.replace(str('C:\\Users\\HP\\Documents\\My_files\\LoopGK\\Syncronik_Internship\\projects\\nomina_app_resetpassword_updated\\nomina_app\\core\\staticfiles\\pdf_files' + '\\' + year_folder), str('fa.syncronik.com'+'/'+year_folder))
        for file_ in files:
            if file_ == file_name:
                return Response({"file": str(directory_name + '/' + file_)}, status=200)
    return Response({"msg": "Archivo no encontrado"}, status=400)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detail_payroll(request):
    file_name = request.data.get('payroll_filename', None)
    # date_pdf = file_name.split('_')[1].split('.pdf')[0]
    # year_folder = date_pdf.split('-')[0]
    
    path = os.path.join(settings.STATIC_ROOT, 'pdf_files')
    for directory_name, directory, files in os.walk(path):
        # directory_name = directory_name.replace(str('C:\\Users\\HP\\Documents\\My_files\\LoopGK\\Syncronik_Internship\\projects\\nomina_app_resetpassword_updated\\nomina_app\\core\\staticfiles\\pdf_files' + '\\' + year_folder), str('fa.syncronik.com'+'/'+year_folder))
        for file_ in files:
            if file_ == file_name:
                return Response({"file": str(directory_name + '/' + file_)}, status=200)
    return Response({"msg": "Archivo no encontrado"}, status=400)
    
