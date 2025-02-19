from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet, MajorViewSet, PersonnelViewSet, AdmissionPeriodViewSet, AwardViewSet, YearViewSet

router = DefaultRouter()
router.register(r'universities', UniversityViewSet)
router.register(r'majors', MajorViewSet)
router.register(r'personnel', PersonnelViewSet)
router.register(r'admission-period', AdmissionPeriodViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'years', YearViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('universities/', UniversityViewSet.as_view({'get': 'list'}), name='universities'),
    path('majors/', MajorViewSet.as_view({'get': 'list'}), name='majors'),
    path('personnel/', PersonnelViewSet.as_view({'get': 'list'}), name='personnel'),
    path('admission-period/', AdmissionPeriodViewSet.as_view({'get': 'list'}), name='admission-period'),
    path('awards/', AwardViewSet.as_view({'get': 'list'}), name='awards'),
    path('years/', YearViewSet.as_view({'get': 'list'}), name='years')
]