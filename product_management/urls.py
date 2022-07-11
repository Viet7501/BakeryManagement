from django.urls import path, include
from rest_framework import routers
from product_management.views import ProductViewSet, HistoryViewSet


router = routers.DefaultRouter()
router.register(prefix='product', viewset=ProductViewSet, basename='product')
router.register(prefix='history', viewset=HistoryViewSet, basename='history')

urlpatterns = [
    path('', include(router.urls)),
]
