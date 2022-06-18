from django.db import models
from organization.models import *


money_banks = (
    ('Money', 'Money'),
    ('Bank', 'Bank'),

)


currency_units = (
    ('$', '$'),
    ('TL', 'TL'),
    ('SOM', 'SOM'),
    ('KON', 'KON'),
)



class ManagerStoreHouse(models.Model):
    name                    = models.CharField(max_length=64, unique=True)
    image                   = models.ImageField(upload_to='manager_images/', null=True, blank=True)
    phone_number            = models.CharField(max_length=16, null=True, blank=True)
    email                   = models.EmailField(null=True, blank=True)
    address                 = models.TextField(null=True, blank=True)
    description             = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"





class OutcomeCategory(models.Model):
    name                    = models.CharField(max_length=256,unique=True)
    seller                  = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.id} -- {self.name}"


class Outcomes(models.Model):
    amount                  = models.IntegerField()
    datetime                = models.DateTimeField(auto_now_add=True)
    customer                = models.ForeignKey(Customer,on_delete=models.CASCADE, blank=True, null=True)
    managerStoreHouse       = models.ForeignKey(ManagerStoreHouse,on_delete=models.CASCADE, blank=True, null=True)
    money_bank              = models.CharField(max_length=32, choices=money_banks)
    currency_unit           = models.CharField(max_length=32, choices=currency_units)
    category                = models.ForeignKey(OutcomeCategory, on_delete=models.CASCADE, null=True)
    description             = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.category.seller}"

    class Meta:
        ordering = ['-datetime']


class IncomeCategory(models.Model):
    name             = models.CharField(max_length=256,unique=True)
    seller             = models.ForeignKey(Seller,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} -- {self.name}"





class Incomes(models.Model):
    amount                  = models.IntegerField()
    note                    = models.TextField()
    datetime                = models.DateTimeField(auto_now_add=True)
    customer                = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    managerStoreHouse       = models.ForeignKey(ManagerStoreHouse, on_delete=models.CASCADE, blank=True, null=True)
    money_bank              = models.CharField(max_length=32, choices=money_banks)
    currency_unit           = models.CharField(max_length=32, choices=currency_units)
    category                = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.category.seller}"
