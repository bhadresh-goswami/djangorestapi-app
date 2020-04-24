from django.db import models

# Create your models here.
class recipe(models.Model):
    recipename = models.CharField(max_length=20)
    ingredients = models.CharField(max_length=200)
    instructions = models.CharField(max_length=1000)
    servingsize = models.IntegerField()
    category = models.CharField(max_length=20)
    notes = models.CharField(max_length=100)
    dateadded = models.DateField()
    datemodified = models.DateField()