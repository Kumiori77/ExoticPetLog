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
    isBeingReared = models.BooleanField(default=True) # 사육중

class Records(models.Model):
    petId = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField("date published")
    weight = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    feeding = models.CharField(null=True, blank=True, max_length=100)
    feededWeight = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    molting = models.BooleanField(default=False)
    image = models.ImageField(upload_to="record", blank=True)

# 대시보드(관리 테이블)
class Dashboard(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    petId = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField("date published")

    class Type(models.TextChoices):
        FEED = "피딩", "피딩"
        DONT_FEED = "피딩 거부", "피딩 거부"
        WAIT_FEED = "피딩 대기", "피딩 대기"
        NONE = "기록 없음", "기록 없음"

    state = models.CharField(max_length=15, choices=Type.choices, default=Type.NONE)