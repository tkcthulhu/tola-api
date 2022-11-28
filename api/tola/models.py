from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    birthday = models.DateField(null=False, default='1990-11-11')

    is_coach = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.username

# class Gym(models.Model):

#     name = models.CharField(max_length=50)

#     street = models.CharField(max_length=100)

#     city = models.CharField(max_length=100)

#     state = models.CharField(max_length=2)
    
#     zipcode = models.IntegerField()
# Create your models here.
