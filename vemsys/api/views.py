from rest_framework.viewsets import ModelViewSet
from .models import Vendor, PurchaseOrder, HistoricalPerformance as HP
from .serializers import VendorSerializer, HistoricalPerformanceSerializer as HPS, PurchaseOrderSerializer
from rest_framework.response import Response


class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PerformanceViewSet(ModelViewSet):
    queryset = HP.objects.all()
    serializer_class = HPS
