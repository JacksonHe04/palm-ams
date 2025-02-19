from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_percent, name='get_percent'),
    path('<int:pk>/', views.update_percent, name='update_percent'),
]