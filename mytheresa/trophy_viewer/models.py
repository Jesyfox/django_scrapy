from django.db import models


class MytheresaItem(models.Model):
    article = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
