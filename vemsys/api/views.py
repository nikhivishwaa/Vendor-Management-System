from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vendor, VendorCode
from .serializers import VendorSerializer
from rest_framework.response import Response


# Create your views here.
class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def perform_create(self, serializer):
        id = VendorCode()
        serializer.vendor_code = id.value()
        serializer.save()

    
