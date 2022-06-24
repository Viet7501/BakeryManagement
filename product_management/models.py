from django.db import models
from django.contrib.auth.models import User
from BakeryManagement.models import TrackingAbstractModel, NameAbstractModel
from product_management.constants import QuantityType


# Create your models here.

class Product(TrackingAbstractModel, NameAbstractModel):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class History(TrackingAbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    action = models.IntegerField(default=QuantityType.ADD, choices=QuantityType.ACTION_CHOICES)

    class Meta:
        verbose_name_plural = 'Histories'

    def __str__(self):
        return f'{self.product.name} - add: {self.action} - expired: {self.quantity} '

    @property
    def status_str(self):
        return QuantityType.ACTION_CHOICES.get(self.action)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.action == 1 and self.product.quantity < self.quantity:
            raise ValueError(
                "Cannot update history because current_quantity < expired_quantity."
            )
        self.price = self.product.price
        super(History, self).save(force_insert, force_update, using, update_fields)
        if self.action == QuantityType.ADD:
            self.product.quantity += self.quantity
        elif self.action == QuantityType.EXPIRED:
            if self.product.quantity < self.quantity:
                raise ValueError(
                    "Cannot update history because current_quantity < expired_quantity."
                )
            else:
                self.product.quantity -= self.quantity
        else:
            if self.quantity > self.product.quantity:
                raise ValueError(
                    "Cannot update history because current_quantity < inventory_quantity."
                )
            else:
                self.product.quantity = self.quantity
        self.product.save()
        # def subtotal():



