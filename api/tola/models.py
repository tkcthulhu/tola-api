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

    weight = models.FloatField(null=False, default=0)
    
    birthday = models.DateField(null=False, default='1990-11-11')

    is_coach = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.username

class user_gym(models.Model):

    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT)

    gym = models.ForeignKey('Gym', on_delete=models.PROTECT)

    date_joined = models.DateField(null=True)

    date_modified = models.DateField(null=True)

    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'gym')


class Gym(BaseModel):

    name = models.CharField(max_length=50)

    street = models.CharField(max_length=100)

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=2)
    
    zipcode = models.IntegerField(
        validators=[
            MinValueValidator(10_000),
            MaxValueValidator(99_999)
        ]
    )

    def __str__(self):
        return self.name

class Exercise(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Max(BaseModel):

    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT)

    exercise = models.ForeignKey('Exercise', on_delete=models.PROTECT)

    num_of_reps = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    weight = models.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(99_999)
        ]
    )

    class Meta:
        unique_together = ('user', 'exercise', 'num_of_reps', 'active')
