from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from api.v1.leagues.models import League
from api.v1.leagues.serializers import LeagueSerializer, LeagueCreateSerializer

# Create your views here.

class LeagueViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the Leagues of the system.
    '''

    queryset = League.objects.all().order_by('-id')
    serializer_class = LeagueSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = LeagueCreateSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)