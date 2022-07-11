from rest_framework import serializers
from money_management.models import Category, Transaction
# Serializers define the API representation.


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Transaction
        fields = ['id', 'category_name', 'amount', 'note']