from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# Create your models here.

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CreatedAbstractModel(models.Model):
    created_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_created_by'
    )
    created_at = models.DateTimeField(
        blank=True, null=True, auto_now=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class ModifiedAbstractModel(models.Model):
    modified_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_modified_by',
    )
    modified_at = models.DateTimeField(
        blank=True, null=True, auto_now=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class TrackingAbstractModel(CreatedAbstractModel, ModifiedAbstractModel):
    class Meta:
        abstract = True


class NameAbstractModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    @staticmethod
    def autocomplete_search_fields():
        return "id__iexact", "name__icontains",

