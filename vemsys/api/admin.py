from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor_code']


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['po_number',
                    'vendor',
                    'order_date',
                    'delivery_date',
                    'status',
                    'quality_rating'
                    ]


@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ['vendor',
                    'quality_rating_avg',
                    'fulfillment_rate',
                    'on_time_delivery_rate'
                    ]
