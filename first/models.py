from django.db import models

# Create your models here.
class Entity(models.Model):
    entity_name = models.CharField(max_length=64)
    entity_country = models.CharField(max_length=64)
    
    def __str__(self):
        return self.entity_name