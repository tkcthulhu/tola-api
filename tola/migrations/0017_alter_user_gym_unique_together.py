# Generated by Django 4.1.3 on 2022-12-01 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0016_alter_user_gym_date_joined'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user_gym',
            unique_together={('user', 'gym')},
        ),
    ]
