from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Bet, BetType
from .serializers import BetSerializer, BetTypeSerializer, BetCreateSerializer

# Create your views here.

class BetTypeViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the Bet-Types of the system.
    '''

    queryset = BetType.objects.all().order_by('-id')
    serializer_class = BetTypeSerializer

class BetViewSet(viewsets.ModelViewSet):
    '''
        This viewset allows to CRUD all the Bets of the system.
    '''

    queryset = Bet.objects.all().order_by('-id')
    serializer_class = BetSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = BetCreateSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)