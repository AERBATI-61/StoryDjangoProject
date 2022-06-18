import decimal
from django.db import models
from django.contrib.auth.models import User
from store.models import *
from invoice.models import *

currency_units = (
    ('$', '$'),
    ('TL', 'TL'),
    ('SOM', 'SOM'),
    ('KON', 'KON'),
)

money_banks = (
    ('Money', 'Money'),
    ('Bank', 'Bank'),
)




class City(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"{self.id} ---  {self.name}"




class Seller(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image               = models.ImageField(upload_to='customer_images/', null=True, blank=True)
    email           = models.EmailField()
    phone           = models.CharField(max_length=32)
    city            = models.ForeignKey(City, on_delete=models.CASCADE, related_name="cities",)
    address         = models.TextField()
    description     = models.TextField(null=True,blank=True)
    date            = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user}"




class Bank(models.Model):
    iban                = models.CharField(max_length=32,null=True,blank=True)
    name                = models.CharField(max_length=64)
    description         = models.TextField(null=True,blank=True)
    organization        = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"









class Customer(models.Model):
    name                = models.CharField(max_length=64,unique=True)
    image               = models.ImageField(upload_to='customer_images/', null=True, blank=True)
    phone_number        = models.CharField(max_length=16,null=True,blank=True)
    email               = models.EmailField(null=True,blank=True)
    address             = models.TextField(null=True,blank=True)
    belongs_to_seller   = models.ForeignKey(Seller, on_delete=models.CASCADE,related_name='belongs_to_seller')
    description         = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def get_product_name(self):
        orderproducts = self.orderitem_set.all()
        product_name = []
        for i in orderproducts:
            product_name.append(i.product.name)
        return product_name



    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.gived_money for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total



class Tax(models.Model):
    tax                     = models.IntegerField(unique=True)

    def __str__(self):
        return str(f'{self.tax} %')











class TransferMoney(models.Model):
    product            = models.ForeignKey('store.Product', on_delete=models.CASCADE, related_name='money_transfer_user')
    customer            = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='money_transfer_user')
    money_bank          = models.CharField(max_length=32, choices=money_banks)
    to_account          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='in_trnafer', null=True, blank=True)
    amount              = models.IntegerField()
    date                = models.DateTimeField(auto_now=True)
    description         = models.TextField(null=True, blank=True)
    currency_unit       = models.CharField(max_length=32, choices=currency_units)


    def __str__(self):
        return self.customer.name

    @property
    def get_product_items(self):
        item = self.customer.get_cart_items
        return item

    @property
    def get_total_money(self):
        item = self.customer.get_cart_total
        return int(item)

    @property
    def get_debt(self):
        debt = self.get_total_money - self.amount
        if (self.get_total_money - self.amount) == 0:
            debt = 0
            return int(debt)
        else:
            return f'{int(debt)} {self.currency_unit}'


    class Meta:
        verbose_name = 'Take Money'




class OrderItem(models.Model):
    product                 = models.ForeignKey("store.Product", on_delete=models.CASCADE, null=True, blank=True)
    customer                = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True)
    tax                     = models.ForeignKey('Tax', on_delete=models.CASCADE, null=True, blank=True)
    quantity                = models.IntegerField(null=True, blank=True, default=0)



    def __str__(self):
        return str(self.product.name)

    @property
    def gived_money(self):
        sell_price = []
        for i in self.product.productinstock_set.all():
            sell_price.append(i.sell_price)

        total = sell_price[0] * self.quantity
        tax = (total * self.tax.tax) / 100
        total = tax + total
        return int(total)

    def products_in_stock(self):
        return self.product.get_rest_product()


    class Meta:
        verbose_name = 'Buy Product'









