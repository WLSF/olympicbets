from rest_framework import serializers
from api.v1.sports.models import Sport

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('id', 'name')