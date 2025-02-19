from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilterSchemeViewSet
from . import views
from . import filter_processor

router = DefaultRouter()
router.register('schemes', FilterSchemeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('process/', filter_processor.process_filters, name='process-filters'),
]