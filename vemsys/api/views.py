from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework.response import Response
from .unique_code import UniqueString


# Create your views here.
class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    def perform_create(self, serializer):
        id = UniqueString()
        serializer.vendor_code = id.name
        serializer.save()
