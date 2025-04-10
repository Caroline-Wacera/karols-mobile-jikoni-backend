from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    ingredients = models.TextField()
    category = models.CharField(max_length=100, default="Uncategorized")

    def __str__(self):
        return self.name