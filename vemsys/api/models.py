from typing import Any, Iterable
from django.db import models
from .unique_code_generator import UniqueCodeGenrator as ucg
from django.db.models import Count, Sum, Avg, F, ExpressionWrapper, DurationField
from django.dispatch import receiver
from django.db.models.signals import post_save


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

    def update_on_time_delivery_rate(self):
        total_completed_orders = self.purchaseorder_set.filter(status='completed').count()
        on_time_delivery_orders = self.purchaseorder_set.filter(
            status='completed', delivery_date__lte=F('acknowledgment_date')
        ).count()
        self.on_time_delivery_rate = (on_time_delivery_orders / total_completed_orders) * 100 if total_completed_orders > 0 else 0
        self.update_historical_performance()
        self.save()

    def update_quality_rating_avg(self):
        completed_orders_with_rating = self.purchaseorder_set.filter(status='completed', quality_rating__isnull=False)
        total_ratings = completed_orders_with_rating.aggregate(total_ratings=Count('quality_rating'))['total_ratings']
        sum_ratings = completed_orders_with_rating.aggregate(sum_ratings=Sum('quality_rating'))['sum_ratings']
        self.quality_rating_avg = sum_ratings / total_ratings if total_ratings > 0 else 0
        self.update_historical_performance()
        self.save()

    def update_average_response_time(self):
        response_times = self.purchaseorder_set.filter(acknowledgment_date__isnull=False).annotate(
            response_time=ExpressionWrapper(
                F('acknowledgment_date') - F('issue_date'),
                output_field=DurationField()
            )
        ).aggregate(avg_response_time=Avg('response_time'))['avg_response_time']
        self.average_response_time = response_times.total_seconds() / response_times.count() if response_times.count() > 0 else 0
        self.update_historical_performance()
        self.save()

    def update_fulfillment_rate(self):
        total_orders = self.purchaseorder_set.count()
        successful_orders = self.purchaseorder_set.filter(status='completed').count()
        self.fulfillment_rate = (successful_orders / total_orders) * 100 if total_orders > 0 else 0
        self.update_historical_performance()
        self.save()

    def update_historical_performance(self):
        HistoricalPerformance.objects.create(
            vendor=self,
            date=F('modified_date'),
            on_time_delivery_rate=self.on_time_delivery_rate,
            quality_rating_avg=self.quality_rating_avg,
            average_response_time=self.average_response_time,
            fulfillment_rate=self.fulfillment_rate,
        )


# purcase order model
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
        super().save()
        # Check if acknowledgment_date is updated
        if self.acknowledgment_date:
            self.vendor.update_average_response_time()

        # Check if the status changed to 'completed'
        if self.status == 'completed':
            self.vendor.update_on_time_delivery_rate()

        # Check if the status changed to 'completed' and a quality rating is provided
        if self.status == 'completed' and self.quality_rating is not None:
            self.vendor.update_quality_rating_avg()

        # Check if the status changed
        if self.status != self._get_orig_status():
            self.vendor.update_fulfillment_rate()


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self) -> str:
        return f"{self.vendor.name} - {self.date}"