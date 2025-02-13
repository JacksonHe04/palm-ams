# Api/front-desk/urls.py
"""
front-desk 应用的路由管理器
"""
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome_view, name='welcome'),
]
