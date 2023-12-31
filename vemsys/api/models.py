from typing import Any, Iterable, Optional
from django.db import models
from .unique_code_generator import UniqueCodeGenrator as ucg


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=10, unique=True, primary_key=True, editable=False)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.name
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        if self.vendor_code == "":
            while True:
                x = 0
                code = ucg.generate(x)
                try:
                    Vendor.objects.get(vender_code = code)
                    x += 1
                except Exception as e:
                    self.vendor_code = code
                    break
        return super().save()


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=15, primary_key=True, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.po_number} - {self.vendor.name}"
    
    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
        if self.po_number == "":
            while True:
                x = 0
                code = ucg.generate(x, max_length=15, random_chars= 4)
                try:
                    Vendor.objects.get(vender_code = code)
                    x += 1
                except Exception as e:
                    self.po_number = code
                    break
        return super().save()

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self) -> str:
        return f"{self.vendor.name} - {self.date}"