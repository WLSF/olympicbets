from rest_framework import serializers

from api.v1.games.models import Game
from api.v1.leagues.serializers import LeagueSerializer
from api.v1.teams.serializers import TeamSerializer


class GameSerializer(serializers.ModelSerializer):
    league = LeagueSerializer(read_only=True)
    teams = TeamSerializer(read_only=True, many=True)   

    class Meta:
        model = Game
        fields = ('id', 'league', 'teams')

class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'league', 'teams')