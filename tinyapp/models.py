from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.

# Create Users models 
class User(AbstractUser):
    pass

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

def __str__(self):
        return f'{self.last_name}, {self.first_name}'
# create url model 
class Url(models.Model):
    short_url = models.URLField(max_length=200)
    long_url = models.URLField(max_length=200)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField('date created')

    def __str__(self):
        return self.short_url

    def get_absolute_url(self):
       return reverse('urls-detail', args=[str(self.pk)])

