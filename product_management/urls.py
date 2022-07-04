from django.urls import path, include
from rest_framework import routers
from product_management.views import ProductViewSet, HistoryViewSet


router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
