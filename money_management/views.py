from money_management.models import Category, Transaction
from rest_framework import viewsets, permissions
from money_management.serializers import CategorySerializer, TransactionSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView
# Create your views here.
# ViewSets define the view behavior.


class CategoryView(ListAPIView, RetrieveAPIView, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
