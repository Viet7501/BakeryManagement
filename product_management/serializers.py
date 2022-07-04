from rest_framework import serializers
from product_management.models import Product, History
# Serializers define the API representation.


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity']


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    product_name = serializers.CharField(source='product.name')

    class Meta:
        model = History
        fields = ['id', 'product_name', 'quantity', 'price', 'action']
