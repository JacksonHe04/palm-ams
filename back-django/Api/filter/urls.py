from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilterSchemeViewSet
from . import views

router = DefaultRouter()
router.register(r'', FilterSchemeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
