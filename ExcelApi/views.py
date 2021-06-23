from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserInfo
from .Serializer import InfoSerializer

import openpyxl

# Create your views here.
# This is particularly cute view allows a user to post and get json of information in  our
# neat little database :)

def putIntoExcel(data):
    wb = openpyxl.Workbook()
    sheet = wb.get_sheet_by_name('Sheet')
    sheet['A1'] = 'Name & Surname'
    sheet['B1'] = 'Contact Number'
    sheet['C1'] = 'Age'
    sheet['D1'] = 'Number Of Children'
    sheet['E1'] = 'Bank ??'

    sheet['A'+ str(data['id'] + 1)] = data['U_Name'] + ' ' + data['U_Surname']
    sheet['B'+ str(data['id'] + 1)] = data['U_ContactNo']
    sheet['C'+ str(data['id'] + 1)] = data['U_Age']
    sheet['D'+ str(data['id'] + 1)] = data['U_ChildCount']
    sheet['E'+ str(data['id'] + 1)] = data['U_BankType']

    wb.save('UserInfo.xlsx')


class UserInfoView(APIView):

    def get(self, request, format=None):
        Info = UserInfo.objects.all()
        serializer = InfoSerializer(Info, many=True)
        return  Response(serializer.data)

    def post(self, request):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            putIntoExcel(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)