from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Create Users models 
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

# create url model 
class Url(models.Model):
    shortUrl = models.CharField(max_length=200)
    longUrl = models.CharField(max_length=50)
    date_created = models.DateTimeField('date created')

class User(AbstractUser):
    pass