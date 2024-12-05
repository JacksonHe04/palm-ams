# Api/home/urls.py
"""
home 应用的路由管理器
"""

# Apply/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.process_form, name='process_form'),
    path('apply_old/', views.process_form_old, name='process_old'),
    path('old/', views.index_old, name='index_old'),
]
