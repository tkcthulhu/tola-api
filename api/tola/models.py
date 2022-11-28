from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class BaseModel(models.Model):

    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    active = models.BooleanField(null=False, default=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser):
    
    birthday = models.DateField(null=False, default='1990-11-11')

    is_coach = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.username

class Gym(BaseModel):

    name = models.CharField(max_length=50)

    street = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=2)
    
    zipcode = models.IntegerField(
        validators=[
            MinValueValidator(99_999),
            MaxValueValidator(10_000)
        ]
    )
# Create your models here.
