# Generated by Django 4.1.3 on 2022-11-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]