from django.db import models
from django.contrib.auth.models import User
from BakeryManagement.models import TrackingAbstractModel, NameAbstractModel


class Category(TrackingAbstractModel, NameAbstractModel):
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.name}'

    def save_name(self):
        self.name = self.name.upper()
        self.save()


class Transaction(TrackingAbstractModel, NameAbstractModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField()
    note = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.category} - {self.amount} - {self.note}'
