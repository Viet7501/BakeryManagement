from rest_framework import serializers
from money_management.models import Category, Transaction
from money_management.report import ReportParams


# Serializers define the API representation.

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class WriteTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['category', 'name', 'amount', 'note']


class ReadTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id', 'category', 'name', 'amount', 'note']


class ReportEntrySerializer(serializers.Serializer):
    category = CategorySerializer()
    total = serializers.DecimalField(max_digits=15, decimal_places=2)
    count = serializers.IntegerField()
    avg = serializers.DecimalField(max_digits=15, decimal_places=2)


class ReportParamsSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return ReportParams(**validated_data)
