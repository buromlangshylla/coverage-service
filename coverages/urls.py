from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoverageViewSet, CustomerCoverageViewSet

router = DefaultRouter()
router.register(r'coverages', CoverageViewSet, basename='coverage')
router.register(r'customer-coverages', CustomerCoverageViewSet, basename='customercoverage')

urlpatterns = [
    path('', include(router.urls)),
]

