from django.urls import path
from . import views

urlpatterns = [
    path('filter/', views.filter_students, name='filter_students'),
]