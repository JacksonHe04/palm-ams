# Api/test/urls.py
"""
test 应用的路由管理器
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apply_post),
    path('get/', views.test_get),
]
