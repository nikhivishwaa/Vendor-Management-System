from rest_framework.serializers import HyperlinkedModelSerializer, ReadOnlyField
from .models import Vendor

class VendorSerializer(HyperlinkedModelSerializer):
    vendor_code = ReadOnlyField()
    class Meta:
        model = Vendor
        fields = "__all__"