from django.urls import path
from . import views

urlpatterns = [
    path('filter/', views.filter_students, name='filter_students'),
    path('failed/', views.get_failed_students, name='get_failed_students'),
]