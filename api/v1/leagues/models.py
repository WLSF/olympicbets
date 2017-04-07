from django.db import models

from api.v1.regions.models import Region
from api.v1.sports.models import Sport

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=20)

    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)