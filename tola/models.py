from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class BaseModel(models.Model):

    created_at = models.DateField(null=True, auto_now_add=True)
    updated_at = models.DateField(null=True, auto_now=True)
    active = models.BooleanField(null=False, default=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser):

    weight = models.FloatField(null=False, default=0, validators=[MinValueValidator(0)])

    units = models.BooleanField(default=False)
    
    birthday = models.DateField(null=False, default='1990-11-11')

    is_coach = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.username

class user_gym(models.Model):

    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT)

    gym = models.ForeignKey('Gym', on_delete=models.PROTECT)

    date_joined = models.DateField(null=True, auto_now_add=True)

    date_modified = models.DateField(null=True, auto_now=True)

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

    def __str__(self):
        return f'{self.user} {self.exercise} {self.active}'

class Program(BaseModel):

    name = models.CharField(max_length=150)

    coach = models.ForeignKey('CustomUser', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class program_session(BaseModel):

    program = models.ForeignKey('Program', on_delete=models.PROTECT)

    week = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(52)
        ]
    )

    session = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(300)
        ]
    )

    def __str__(self):
        return f'{self.program} session:{self.session}'

class program_session_exercise(BaseModel):

    program_session = models.ForeignKey('program_session', on_delete=models.PROTECT)

    order = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )

    exercise = models.ForeignKey('Exercise', on_delete=models.PROTECT, related_name='exercise')

    max_exercise = models.ForeignKey('Exercise', on_delete=models.PROTECT, related_name='max_exercise')

    def __str__(self):
        return f'{self.program_session} {self.exercise}'

class program_session_exercise_set(BaseModel):

    program_session_exercise = models.ForeignKey('program_session_exercise', on_delete=models.PROTECT)

    set_num = models.IntegerField()

    num_of_reps = models.CharField(max_length=6)

    percent = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )

    def __str__(self):
        return f'{self.program_session_exercise} set:{self.set_num} {self.percent}%'

class user_program(BaseModel):

    athlete = models.ForeignKey('CustomUser', on_delete=models.PROTECT)

    program = models.ForeignKey('Program', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('athlete', 'program', 'active')

class SetStatus(models.Model):

    status = models.CharField(max_length=15)

class user_set(BaseModel):

    athlete = models.ForeignKey('CustomUser', on_delete=models.PROTECT)

    session_set = models.ForeignKey('program_session_exercise_set', on_delete=models.PROTECT)

    status = models.ForeignKey('SetStatus', on_delete=models.PROTECT)

