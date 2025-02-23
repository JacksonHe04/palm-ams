from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.InterviewUploadView.as_view(), name='interview-upload'),
    path('normalized', views.get_normalized_scores, name='interview-normalized'),
]