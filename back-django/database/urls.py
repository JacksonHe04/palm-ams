# database/urls.py
"""
database 应用的路由管理器
"""
from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_data, name='apply_data'),
    path('files/', views.files_data, name='files_data'),
]
