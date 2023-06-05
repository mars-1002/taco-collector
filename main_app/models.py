from django.db import models
from django.urls import reverse

class Taco(models.Model):
    name = models.CharField(max_length=100)
    meat = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    order = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("taco-detail", kwargs={"taco_id": self.id})
    