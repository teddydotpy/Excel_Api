from django.urls import path
from .views import UserInfoView

patterns = [
    path('', UserInfoView.as_view()),
]