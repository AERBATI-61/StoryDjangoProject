from django.urls import path
from .views import *

urlpatterns = [
    path('invoice_list/', InvoiceList.as_view(), name="invoice_list"),
    # path('invoice_create/', ProductInStockCreate.as_view(), name="invoice_create"),
    # path('stock_update/<int:id>/', StockUpdate.as_view(), name="stock_update"),
    # path('stock_delete/<int:id>/', StockDelete.as_view(), name="stock_delete"),
    path('invoice_detail/<int:id>/', InvoiceDetail.as_view(), name="invoice_detail"),

    path('customer_list/', CustomerList.as_view(), name="customer_list"),
    # path('product_create_in_stock/', ProductInStockCreate.as_view(), name="product_create_in_stock"),
    # path('stock_update/<int:id>/', StockUpdate.as_view(), name="stock_update"),
    # path('stock_delete/<int:id>/', StockDelete.as_view(), name="stock_delete"),

    path('payment_list/', PaymentList.as_view(), name="payment_list"),
    # path('product_create_in_stock/', ProductInStockCreate.as_view(), name="product_create_in_stock"),
    # path('stock_update/<int:id>/', StockUpdate.as_view(), name="stock_update"),
    # path('stock_delete/<int:id>/', StockDelete.as_view(), name="stock_delete"),


]