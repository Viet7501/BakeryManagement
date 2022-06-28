from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product_management.views import ProductViewSet, HistoryViewSet


router = routers.DefaultRouter()
router.register(r'Product', ProductViewSet)
router.register(r'History', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]