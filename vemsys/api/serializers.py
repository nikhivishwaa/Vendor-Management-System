from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Vendor

class VendorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"