from django.db import models

from api.v1.users.models import User
from api.v1.games.models import Game

# Create your models here.

class ConcludedBetsManager(models.Manager):
    def get_queryset(self):
        return super(ConcludedBetsManager, self).get_queryset().filter(result=True)

class BetType(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bet(models.Model):
    user = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_user", on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    bet_type = models.ForeignKey(BetType, on_delete=models.CASCADE)
    
    result = models.BooleanField(default=False)
    result_date = models.DateTimeField(null=True)
    admin = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_admin", on_delete=models.CASCADE, null=True)

    value = models.DecimalField(max_digits=10, decimal_places=2)
    odd = models.DecimalField(max_digits=4, decimal_places=2)
    combined = models.CharField(max_length=50, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)