from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    wallet = models.IntegerField(default=10000)

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=800)
    price = models.PositiveIntegerField(default=0)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'id_{self.id} | {self.name}'