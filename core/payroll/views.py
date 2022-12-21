# from django.shortcuts import render
from rest_framework.decorators import api_view
# from rest_framework import status
from rest_framework.response import Response
from django.conf import settings

from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
import os
 
# Create your views here.
@api_view(['POST']) 
def payrolls_register(request):
 
        s = StaticFilesStorage()
        files = list(get_files(s, location='pdf_files/2020'))

        # file name with extension
        # path = os.path.basename('/pdf_files/2020')
        # file_name = os.path.basename('../pdf_files/2020/NOM1221_2020-01-01.pdf')
        
        # file name without extension
        # print(os.path.splitext(file_name)[0])

        # path='../pdf_files/2020/NOM1221_2020-01-01.pdf' 
        # print(os.path.basename(path))

        # path = settings.STATIC_URL
        return Response({
                # "ruta": os.path.splitext(file_name)[0]
                # "ruta": settings.STATIC_URL
                "ruta": files
        })
        # print(settings.STATIC_URL)

# payrolls_register()