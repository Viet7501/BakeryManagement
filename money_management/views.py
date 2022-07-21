from money_management.models import Category, Transaction
from rest_framework import viewsets, permissions
from money_management.serializers import CategorySerializer, WriteTransactionSerializer, ReadTransactionSerializer, ReportEntrySerializer, ReportParamsSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from money_management.report import transaction_report
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
# ViewSets define the view behavior.


class CategoryView(ListAPIView, RetrieveAPIView, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionViewSet(ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadTransactionSerializer
        return WriteTransactionSerializer


class TransactionReportAPIView(APIView):
    def get(self, request):
        params_serializer = ReportParamsSerializer(data=request.GET, context={"request": request})
        params_serializer.is_valid(raise_exception=True)
        params = params_serializer.save()
        data = transaction_report(params)
        serializer = ReportEntrySerializer(instance=data, many=True)
        return Response(data=serializer.data)
