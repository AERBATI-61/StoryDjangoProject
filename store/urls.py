from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('store/', storeView, name='storeView'),
    path('', timeView, name="timeView"),


    path('product-list/', ProductList.as_view(), name="product_list"),
    path('product/<slug:slug>', ProductDetail.as_view(), name="product_detail"),
    path('product-list/<slug:slug>', product_view_with_category, name="category_view_with_category"),
    path('product_create/', ProductCreate.as_view(), name="product_create"),
    path('product_update/<slug:slug>', ProductUpdate.as_view(), name="product_update"),
    path('product_delete/<slug:slug>', ProductDelete.as_view(), name="product_delete"),


    path('category_list/', CategoryList.as_view(), name="category_list"),
    path('category_create/', CategoryCreate.as_view(), name="category_create"),
    path('category_update/<int:id>/', CategoryUpdate.as_view(), name="category_update"),
    path('category_delete/<int:id>/', CategoryDelete.as_view(), name="category_delete"),








    path('stock-list/', ProductInStockList.as_view(), name="stock_list"),
    path('product_create_in_stock/', ProductInStockCreate.as_view(), name="product_create_in_stock"),
    path('stock_update/<int:id>/', StockUpdate.as_view(), name="stock_update"),
    path('stock_delete/<int:id>/', StockDelete.as_view(), name="stock_delete"),




    path('tax_list/', TaxList.as_view(), name="tax_list"),
    path('tax_create/', TaxCreate.as_view(), name="tax_create"),
    path('tax_update/<int:id>/', TaxUpdate.as_view(), name="tax_update"),
    path('tax_delete/<int:id>/', TaxDelete.as_view(), name="tax_delete"),

]
