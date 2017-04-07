from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from api.v1.games.models import Game
from api.v1.games.serializers import GameSerializer, GameCreateSerializer

# Create your views here.

class GameViewSet(viewsets.ModelViewSet):

    queryset = Game.objects.all().order_by('-id')
    serializer_class = GameSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = GameCreateSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)