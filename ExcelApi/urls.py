from django.urls import path
from . import views

patterns = [
    path('Info/', views.UserInfoView.as_view(), name='info'),
    path('', views.indexView.as_view(), name='index'),
]