from django.contrib.auth.models import User, Group
from rest_framework import serializers
from product_management.models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity']