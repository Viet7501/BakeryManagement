from product_management.models import Product, History
from rest_framework import viewsets
from rest_framework import permissions
from product_management.serializers import ProductSerializer, HistorySerializer


# Create your views here.
# ViewSets define the view behavior.


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = History.objects.all().order_by('-id')
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]
