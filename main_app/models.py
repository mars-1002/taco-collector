from django.db import models

class Taco(models.Model):
    name = models.CharField(max_length=100)
    meat = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    order = models.IntegerField()

    def __str__(self):
        return self.name