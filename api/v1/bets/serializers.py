from rest_framework import serializers

from api.v1.bets.models import Bet, BetType
from api.v1.users.serializers import UserSerializer
from api.v1.games.serializers import GameSerializer


class BetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetType
        fields = ('id', 'name', 'description')


class BetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    game = GameSerializer(read_only=True, many=True)   
    bettype = BetTypeSerializer(read_only=True)

    class Meta:
        model = Bet
        fields = ('id', 'user', 'game', 'value', 'odd', 'bettype', 'combined')