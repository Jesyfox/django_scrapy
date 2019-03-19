from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MytheresaItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = ArrayField(models.URLField())
    price = models.CharField(max_length=100)
    size = ArrayField(models.CharField(max_length=100))
    description = models.TextField()
