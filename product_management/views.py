from django.shortcuts import render
from django.contrib.auth.models import User
from product_management.models import Product
from rest_framework import viewsets
from rest_framework import permissions
from product_management.serializers import UserSerializer, ProductSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
