from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ["barcode", "name", "datetime", "get_rest_product"]
    list_display_links = ["barcode", "name", "datetime"]
    search_fields = ["barcode", "name", "datetime"]

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["productCategory"]


class ProductInStockAdmin(admin.ModelAdmin):
    list_display = ["product", "count", "price", "currency_unit", "sell_price", "datetime", "products_in_stock"]












admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)


admin.site.register(ProductInStock, ProductInStockAdmin)

