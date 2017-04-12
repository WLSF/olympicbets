from django.db import models

from api.v1.leagues.models import League
from api.v1.teams.models import Team

# Create your models here.

class Game(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)