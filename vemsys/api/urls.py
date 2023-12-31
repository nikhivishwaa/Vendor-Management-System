from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet, PerformanceViewSet
from . import views

router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)
# router.register(r'vendors', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]