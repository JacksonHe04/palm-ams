from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet, MajorViewSet, PersonnelViewSet, AdmissionPeriodViewSet

router = DefaultRouter()
router.register(r'universities', UniversityViewSet)
router.register(r'majors', MajorViewSet)
router.register(r'personnel', PersonnelViewSet)
router.register(r'admission-period', AdmissionPeriodViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('universities/', UniversityViewSet.as_view({'get': 'list'}), name='universities'),
    path('majors/', MajorViewSet.as_view({'get': 'list'}), name='majors'),
    path('personnel/', PersonnelViewSet.as_view({'get': 'list'}), name='personnel'),
    path('admission-period/', AdmissionPeriodViewSet.as_view({'get': 'list'}), name='admission-period'),
]