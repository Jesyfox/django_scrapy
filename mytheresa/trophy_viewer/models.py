from django.contrib.postgres.fields import ArrayField
from django.db import models


class MytheresaItem(models.Model):
    article = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = ArrayField(models.CharField(max_length=100))
    price = models.CharField(max_length=100)
    size = ArrayField(models.CharField(max_length=100))
    description = models.TextField()
