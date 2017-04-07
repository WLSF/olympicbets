from django.shortcuts import render

from rest_framework import viewsets

from api.v1.sports.serializers import SportSerializer
from api.v1.sports.models import Sport

# Create your views here.

class SportViewSet(viewsets.ModelViewSet):

    queryset = Sport.objects.all().order_by('-id')
    serializer_class = SportSerializer