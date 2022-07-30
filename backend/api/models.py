from django.db import models

# Create your models here.
class Entity(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name