# Generated by Django 4.1.3 on 2022-11-28 15:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0003_customuser_is_coach_alter_customuser_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.IntegerField(validators=[django.core.validators.MinValueValidator(99999), django.core.validators.MaxValueValidator(10000)])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
