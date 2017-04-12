from rest_framework import serializers

from api.v1.results.models import Result, ResultType
from api.v1.games.serializers import GameSerializer
from api.v1.teams.serializers import TeamSerializer


class ResultTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultType
        fields = ('id', 'name')

class ResultSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    team = TeamSerializer(read_only=True)   
    result_type = ResultTypeSerializer(read_only=True)

    class Meta:
        model = Result
        fields = ('id', 'game', 'team', 'result_type', 'value')