from rest_framework import serializers

from api.v1.leagues.models import League

from api.v1.sports.serializers import SportSerializer
from api.v1.regions.serializers import RegionSerializer

class LeagueSerializer(serializers.ModelSerializer):
    sport = SportSerializer(read_only=True)
    region = RegionSerializer(read_only=True)

    class Meta:
        model = League
        fields = ('id', 'name', 'sport', 'region')

class LeagueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('id', 'name', 'sport', 'region')