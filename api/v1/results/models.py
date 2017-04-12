from django.db import models

from api.v1.games.models import Game
from api.v1.teams.models import Team

# Create your models here.

class ResultType(models.Model):
    name = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Result(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    result_type = models.ForeignKey(ResultType, on_delete=models.CASCADE)
    
    value = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)