from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    instance.vendor.update_on_time_delivery_rate()
    instance.vendor.update_quality_rating_avg()
    instance.vendor.update_average_response_time()
    instance.vendor.update_fulfillment_rate()
