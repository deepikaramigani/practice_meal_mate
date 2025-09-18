from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=30)

class Restaurant(models.Model):
    name=models.CharField(max_length=20)
    picture=models.URLField(max_length=500)
    cuisine=models.CharField(max_length=20)
    rating=models.FloatField()
