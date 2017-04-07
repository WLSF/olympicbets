from django.shortcuts import render

from rest_framework import viewsets

from api.v1.users.models import User
from api.v1.users.serializers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    '''
        User ModelViewSet
    '''

    queryset = User.objects.all()
    serializer_class = UserSerializer

    