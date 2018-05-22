from django.db import models

# Create your models here.
class Flight(models.Model):
    enity_name = models.CharField(max_length=64)
    entity_country = models.CharField(max_length=64)
    