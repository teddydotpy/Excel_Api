from django.urls import path
from .views import UserInfoView
from .views import index
from .views import req_resolution

patterns = [
    path('Info/', UserInfoView.as_view()),
    path('NormalForm/', req_resolution, name='Normal Form'),
    path('', index, name='index'),
]