# Api/home/urls.py
"""
home 应用的路由管理器
"""
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome_view, name='welcome'),
]
