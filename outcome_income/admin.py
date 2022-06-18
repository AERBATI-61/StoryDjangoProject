from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class OutcomesCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "seller"]

admin.site.register(OutcomeCategory, OutcomesCategoryAdmin)




class OutcomesAdmin(admin.ModelAdmin):
    list_display = ["category", "amount", "currency_unit", "customer", "managerStoreHouse", "datetime"]


admin.site.register(Outcomes, OutcomesAdmin)





class IncomesCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "seller",]
admin.site.register(IncomeCategory, IncomesCategoryAdmin)


class IncomesAdmin(admin.ModelAdmin):
    list_display = ["category", "amount", "currency_unit", "customer", "managerStoreHouse", "datetime"]

admin.site.register(Incomes, IncomesAdmin)









admin.site.register(ManagerStoreHouse)
