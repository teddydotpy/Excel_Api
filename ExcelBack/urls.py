from django.contrib import admin
from django.urls import path, include, re_path
from ExcelApi.urls import patterns
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    re_path(r'Info/', include(patterns)),
]
