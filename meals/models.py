from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    ingredients = models.TextField()
