from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class User(AbstractUser):
   
    def __str__(self):
        return self.username

class Pet(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=200)

class Records(models.Model):
    petId = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField("date published")
    weight = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    feeding = models.CharField(null=True, blank=True, max_length=100)
    feededWeight = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    molting = models.BooleanField(default=False)