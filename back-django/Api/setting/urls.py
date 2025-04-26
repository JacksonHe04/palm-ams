from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet, MajorViewSet, PersonnelViewSet, AwardViewSet, YearViewSet

router = DefaultRouter()
router.register(r'universities', UniversityViewSet)
router.register(r'majors', MajorViewSet)
router.register(r'personnel', PersonnelViewSet)
router.register(r'awards', AwardViewSet)
router.register(r'year', YearViewSet)

urlpatterns = [
    path('', include(router.urls)),
]