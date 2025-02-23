from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('user_info/', views.user_info, name='user_info'),
]