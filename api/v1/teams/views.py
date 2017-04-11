from django.shortcuts import render

from rest_framework import viewsets

from api.v1.teams.models import Team
from api.v1.teams.serializers import TeamSerializer

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the Teams of the system.
    '''

    queryset = Team.objects.all().order_by('-id')
    serializer_class = TeamSerializer