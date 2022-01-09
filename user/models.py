from django.db import models

# Create your models here.

class user(models.Model):
    userId    = models.AutoField(primary_key=True)
    Email     = models.CharField(max_length=100)
    firstName = models.CharField(max_length=10)
    lastName  = models.CharField(max_length=10)
    password  = models.CharField(max_length=20)
class product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    price = models.IntegerField()


    
