from money_management.models import Category, Transaction
from rest_framework import viewsets
from rest_framework import permissions
from money_management.serializers import CategorySerializer, TransactionSerializer


# Create your views here.
# ViewSets define the view behavior.


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.BasePermission]


class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Transaction.objects.all().order_by('-id')
    serializer_class = TransactionSerializer
    permission_classes = [permissions.BasePermission]
