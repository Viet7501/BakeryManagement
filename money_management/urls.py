from django.urls import path, include
from rest_framework import routers
from money_management.views import CategoryViewSet, TransactionViewSet


router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
