from django.shortcuts import render

from rest_framework import viewsets

from api.v1.regions.models import Region
from api.v1.regions.serializers import RegionSerializer

# Create your views here.

class RegionViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the Regions of the system.
    '''

    queryset = Region.objects.all().order_by('-id')
    serializer_class = RegionSerializer