from django.db import models
from django.contrib.auth.models import User
from BakeryManagement.models import TrackingAbstractModel, NameAbstractModel


# Create your models here.

class Product(TrackingAbstractModel, NameAbstractModel):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class History(TrackingAbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory_quantity = models.IntegerField(null=False)
    add_quantity = models.IntegerField(null=True)
    expired_quantity = models.IntegerField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        verbose_name_plural = 'Histories'

    def __str__(self):
        return f'{self.product.name} - add: {self.add_quantity} - expired: {self.expired_quantity} '

    @property
    def subtotal(self):
        return (self.product.quantity + self.add_quantity - self.expired_quantity - self.inventory_quantity) * self.price