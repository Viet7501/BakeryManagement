from django.urls import path, include
from rest_framework import routers
from money_management.views import CategoryView, TransactionViewSet


router = routers.DefaultRouter()
router.register(prefix='transaction', viewset= TransactionViewSet, basename='transaction')
router.register(prefix=r'category', viewset=CategoryView, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
