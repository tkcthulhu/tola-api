# Generated by Django 4.1.3 on 2022-12-06 13:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0027_program_session_week_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program_session',
            name='day',
        ),
        migrations.AddField(
            model_name='program_session',
            name='session',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(300)]),
            preserve_default=False,
        ),
    ]
