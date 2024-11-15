# Api/test/urls.py
"""
test 应用的路由管理器
"""
from django.urls import path
from . import views

urlpatterns = [
    path('test_get/', views.test_get, name='example'),
    path('test_post/', views.test_post, name='example'),
]
