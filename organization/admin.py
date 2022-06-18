from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from .models import *
from store.models import *
from django.http import HttpResponseRedirect



class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "belongs_to_seller", "get_cart_total", "get_cart_items", "selected_get_product_name"]

    def selected_get_product_name(self, obj):
        html = "<ul>"
        for product_name in obj.get_product_name:
            html += "<li>" + product_name + "</li>"
        html += "</ul>"
        return mark_safe(html)
admin.site.register(Customer, CustomerAdmin)









class orderAdmin(admin.ModelAdmin):
    list_display = ["customer", "product", "quantity", "gived_money"]
    readonly_fields = ["products_in_stock"]

    def response_change(self, request, obj, post_url_continue=None):
        for i in Product.objects.all():
            if i.get_rest_product() <= 0:
                messages.add_message(request, messages.WARNING, f'Not Saved')
                return HttpResponseRedirect(request.path_info)
            else:
                messages.add_message(request, messages.SUCCESS, f'successfully Saved')
                return HttpResponseRedirect('http://127.0.0.1:8000/admin/organization/orderitem/')

admin.site.register(OrderItem, orderAdmin)



class TransferMoneyAdmin(admin.ModelAdmin):
    list_display = ["customer", "product",  "money_bank", "to_account", "amount", "get_total_money", "get_debt", "get_product_items", "date"]
    readonly_fields = ["get_product_items", "get_total_money", "get_debt"]

admin.site.register(TransferMoney, TransferMoneyAdmin)





admin.site.register(Bank)
admin.site.register(City)
admin.site.register(Tax)
admin.site.register(Seller)