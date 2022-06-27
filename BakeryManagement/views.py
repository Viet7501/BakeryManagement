from BakeryManagement.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.BasePermission]
