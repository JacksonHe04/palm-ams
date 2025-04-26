from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdmissionDateViewSet

router = DefaultRouter()
router.register(r'admission-dates', AdmissionDateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]