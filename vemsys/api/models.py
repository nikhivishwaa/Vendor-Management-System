from typing import Any
from django.db import models


# Model for vendors
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(
        max_length=10,
        primary_key=True,
        null=False,
        editable=False,
        db_index=True,
    )
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name
