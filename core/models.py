from django.db import models
from django.contrib.auth.models import User

class Assets(models.Model):
    code = models.SlugField()
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class RegisteredAssets(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Assets, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=255, decimal_places=2)
    minimum_price = models.DecimalField(max_digits=255, decimal_places=2)
    maximum_price = models.DecimalField(max_digits=255, decimal_places=2)
    frequency = models.IntegerField(max_length=3)

