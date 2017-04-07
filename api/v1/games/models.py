from django.db import models

from api.v1.leagues.models import League
from api.v1.teams.models import Team

# Create your models here.

class Game(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team,  through='GameTeams')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GameTeams(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)