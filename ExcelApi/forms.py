from django import forms

class Userform(forms.Form):
    Name = forms.CharField(max_length=30, required=True)
    Surname = forms.CharField(max_length=30, required=True)
    Age = forms.IntegerField(required=True)
    Contact_Number = forms.IntegerField(required=True)
    Number_of_Children = forms.IntegerField(required=True)
    Bank_Name = forms.CharField(max_length=30, required=True)