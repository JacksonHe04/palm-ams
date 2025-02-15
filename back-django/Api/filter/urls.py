from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilterSchemeViewSet
from . import views

router = DefaultRouter()
router.register(r'filter-schemes', FilterSchemeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filter-schemes/', views.filter_schemes, name='filter_schemes'),
]
