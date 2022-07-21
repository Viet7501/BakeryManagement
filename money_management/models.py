from django.db import models
from django.contrib.auth.models import User
from BakeryManagement.models import TrackingAbstractModel, NameAbstractModel
from money_management.constants import CategoryChoice


class Category(TrackingAbstractModel, NameAbstractModel):
    category_choices = models.IntegerField(default=0, choices=CategoryChoice.CATEGORY_CHOICES)

    class Meta:
        verbose_name_plural = "Categories"

    @property
    def class_choices_str(self):
        return CategoryChoice.CATEGORY_CHOICES_DICT.get(self.category_choices)

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
