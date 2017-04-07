from django.shortcuts import render

from rest_framework import viewsets

from api.v1.leagues.models import League
from api.v1.leagues.serializers import LeagueSerializer

# Create your views here.

class LeagueViewSet(viewsets.ModelViewSet):

    queryset = League.objects.all().order_by('-id')
    serializer_class = LeagueSerializer