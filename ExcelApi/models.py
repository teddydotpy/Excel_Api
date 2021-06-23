from django.db import models

# User model it is supposed to create a database that has these columns.
class UserInfo(models.Model):
    U_Name = models.CharField(max_length=30, null=True, blank=False)
    U_Surname = models.CharField(max_length=30, null=True, blank=False)
    U_Age = models.IntegerField(blank=True, null=True)
    U_ContactNo = models.IntegerField( blank=True, null=True)
    U_ChildCount = models.IntegerField(blank=True, null=True)
    U_BankType = models.TextField(max_length=50, blank=True, null=True)
