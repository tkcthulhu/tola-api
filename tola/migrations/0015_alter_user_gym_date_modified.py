# Generated by Django 4.1.3 on 2022-12-01 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0014_alter_user_gym_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_gym',
            name='date_modified',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
