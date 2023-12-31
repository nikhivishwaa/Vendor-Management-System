from django.urls import path
from .views import VendorListCreateView, VendorDetailsView, PurchaseOrderListCreateView, PurchaseOrderDetailsView, VendorPerformanceView, AcknowledgePurchaseOrderView

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<str:pk>/', VendorDetailsView.as_view(), name='vendor-details'),
    path('vendors/<str:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<str:pk>/', PurchaseOrderDetailsView.as_view(), name='purchase-order-details'),
    path('purchase_orders/<str:pk>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),
]