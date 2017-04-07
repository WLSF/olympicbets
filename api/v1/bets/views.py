from django.shortcuts import render

from rest_framework import viewsets

from .models import Bet, BetType
from .serializers import BetSerializer, BetTypeSerializer

# Create your views here.

class BetTypeViewSet(viewsets.ModelViewSet):
    queryset = BetType.objects.all().order_by('-id')
    serializer_class = BetTypeSerializer

class BetViewSet(viewsets.ModelViewSet):

    queryset = Bet.objects.all().order_by('-id')
    serializer_class = BetSerializer