from rest_framework import serializers
from api.v1.leagues.models import League

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('id', 'name')