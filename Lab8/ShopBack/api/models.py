from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'
