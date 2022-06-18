from django.db import models
from django.template.defaultfilters import slugify
from organization.models import *

currency_units = (
    ('$', '$'),
    ('TL', 'TL'),
    ('SOM', 'SOM'),
    ('KON', 'KON'),
)

money_banks = (
    ('Money', 'Money'),
    ('Bank', 'Bank'),
    ('Paid', 'Paid'),

)


class ProductCategory(models.Model):
    category               = models.CharField(max_length=64)
    slug                          = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category



class Product(models.Model):
    barcode                       = models.CharField(max_length=64, unique=True)
    name                          = models.CharField(max_length=64, unique=True)
    category                      = models.ManyToManyField(ProductCategory)
    count                         = models.IntegerField()
    buy_price                     = models.IntegerField()
    sell_price                    = models.IntegerField()
    currency_unit                 = models.CharField(max_length=32, choices=currency_units, blank=True, null=True)
    datetime                      = models.DateTimeField(auto_now=True)
    image                         = models.ImageField(upload_to='product_images/', null=True, blank=True)
    description                   = models.TextField(max_length=512, null=True, blank=True)
    slug                          = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)


    def __str__(self):
        return f"{self.name}"

    def get_rest_product(self):
        quantity = 0
        orderitem_quentitys = self.orderitem_set.all()
        orderitem_quentity = sum([item.quantity for item in orderitem_quentitys])
        productinstock_quentities = self.productinstock_set.all()
        productinstock_quentity = sum([item.count for item in productinstock_quentities])
        if (productinstock_quentity - orderitem_quentity) < 0:
            return quantity
        else:
            quantity = productinstock_quentity - orderitem_quentity
            return quantity




    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-datetime']







class ProductInStock(models.Model):
    product                  = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, default=0)
    count                    = models.IntegerField()
    price                    = models.IntegerField()
    sell_price               = models.IntegerField()
    currency_unit            = models.CharField(max_length=32, choices=currency_units, blank=True, null=True)
    datetime                 = models.DateTimeField(auto_now=True)

    def products_in_stock(self):
        return self.product.get_rest_product()


    class Meta:
        verbose_name = 'Products From Stock'