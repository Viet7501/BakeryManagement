from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from money_management.views import CategoryViewSet, TransactionViewSet


router = routers.DefaultRouter()
router.register(r'Category', CategoryViewSet)
router.register(r'Transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]