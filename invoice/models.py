from django.db import models
from organization.models import *
from store.models import *


class Invoice(models.Model):
    description = models.TextField(null=True, blank=True)
    inv_no = models.CharField(max_length=128, null=True, blank=True)
    customer = models.ForeignKey("organization.Customer", on_delete=models.CASCADE,
                                 null=True, blank=True)
    user = models.ForeignKey("organization.Seller", on_delete=models.CASCADE, related_name='invoice_user')
    datetime = models.DateTimeField()
    tax = models.ForeignKey("organization.Tax", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user} - For - {self.customer}"

    @property
    def gived_money(self):
        total = SoldProduct.objects.all()
        t = []
        for i in total:
            t.append(i.price * i.count)
        tax = (t[0] * self.tax.tax) / 100
        to = tax + t[0]
        return int(to)

    # @property
    # def get_debt(self):
    #     debt = self.gived_money - self.amount
    #     if (self.get_total_money - self.amount) == 0:
    #         debt = 0
    #         return int(debt)
    #     else:
    #         return f'{int(debt)} {self.currency_unit}'


class SoldProduct(models.Model):
    product = models.ForeignKey("store.Product", on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("organization.Seller", on_delete=models.CASCADE)
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.product} ----- Price - {self.price} SAR "

    @property
    def gived_money(self):
        total = self.price * self.count
        tax = (total * self.invoice.tax.tax) / 100
        total = tax + total
        return int(total)




class ReturnedProduct(models.Model):
    sold_product = models.ForeignKey("SoldProduct", on_delete=models.CASCADE)
    customer = models.ForeignKey("organization.Customer", on_delete=models.CASCADE,
                                 null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    note = models.TextField(null=True, blank=True)


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    bank = models.ForeignKey('organization.Bank', on_delete=models.DO_NOTHING,
                             blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()
    note = models.TextField(null=True, blank=True)
    user = models.ForeignKey("organization.Seller", on_delete=models.CASCADE, related_name='payment_INVOICE_user')
    customer = models.ForeignKey("organization.Customer", on_delete=models.CASCADE, related_name='invoice_customer',
                                 null=True, blank=True)



    def __str__(self):
        return f"{self.user.user} {self.customer.name} SAR --- For - {self.amount}"

