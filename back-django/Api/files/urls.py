from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<str:file_id>/', views.download_file, name='download_file'),
    path('delete/<str:file_id>/', views.delete_file, name='delete_file'),
    path('info/<str:file_id>/', views.get_file_info, name='get_file_info'),
]