from django.shortcuts import render

from rest_framework import viewsets

from api.v1.games.models import Game
from api.v1.games.serializers import GameSerializer

# Create your views here.

class GameViewSet(viewsets.ModelViewSet):

    queryset = Game.objects.all().order_by('-id')
    serializer_class = GameSerializer