from django.db import models

# Create your models here.
class Group(models.Model):
    code = models.CharField(max_length=3)
    group_name = models.CharField(max_length=64)

    def __str__(self):
        return self.group_name

class Entity(models.Model):
    entity_name = models.CharField(max_length=64)
    entity_group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="origin")
    
    def __str__(self):
        return self.entity_name
        
        
      
