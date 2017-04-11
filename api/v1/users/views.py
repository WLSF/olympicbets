from django.shortcuts import render

from rest_framework import viewsets

from api.v1.users.models import User
from api.v1.users.serializers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the Users of the system.

        The users created can be regular or admin.
    '''

    queryset = User.objects.all()
    serializer_class = UserSerializer

    