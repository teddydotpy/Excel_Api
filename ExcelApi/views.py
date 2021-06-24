from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import Userform

from .models import UserInfo
from .Serializer import InfoSerializer

import openpyxl
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
# This is particularly cute view allows a user to post and get json of information in  our
# neat little database :)

def index(request):
    return render(request, 'pages/index.html', {'form': Userform})

def req_resolution(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Userform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('pages/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Userform()

    return render(request, 'pages/index.html', {'form': Userform})

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


def NormalExcel(data):
    wb = openpyxl.Workbook()
    sheet = wb.get_sheet_by_name('Sheet')
    sheet['A1'] = 'Name & Surname'
    sheet['B1'] = 'Contact Number'
    sheet['C1'] = 'Age'
    sheet['D1'] = 'Number Of Children'
    sheet['E1'] = 'Bank ??'

    sheet['A'+ str(UserInfo.objects.latest('id').id + 1)] = data['Name'] + ' ' + data['Surname']
    sheet['B'+ str(UserInfo.objects.latest('id').id + 1)] = data['Contact_Number']
    sheet['C'+ str(UserInfo.objects.latest('id').id + 1)] = data['Age']
    sheet['D'+ str(UserInfo.objects.latest('id').id + 1)] = data['Number_of_Children']
    sheet['E'+ str(UserInfo.objects.latest('id').id + 1)] = data['Bank_Name']

    wb.save('UserInfo.xlsx')


class UserInfoView(APIView):

    def get(self, request, format=None):
        Info = UserInfo.objects.all()
        serializer = InfoSerializer(Info, many=True)
        return  Response(serializer.data)

    def post(self, request):
        form = Userform(request.POST)
        if form.is_valid():
            print(request.data)
            new_post = UserInfo(
                U_Name = request.data['Name'],
                U_Surname = request.data['Surname'],
                U_Age = request.data['Age'],
                U_ContactNo = request.data['Contact_Number'],
                U_ChildCount = request.data['Number_of_Children'],
                U_BankType = request.data['Bank_Name'],
            )
            new_post.save()
            NormalExcel(request.data)
            Response(request.data, status=status.HTTP_201_CREATED)
            return HttpResponseRedirect('..', {'form': Userform})

        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            putIntoExcel(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
