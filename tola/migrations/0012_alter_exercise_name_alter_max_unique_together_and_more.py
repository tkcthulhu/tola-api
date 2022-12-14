# Generated by Django 4.1.3 on 2022-11-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0011_max'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='max',
            unique_together={('user', 'exercise', 'num_of_reps', 'active')},
        ),
        migrations.AlterUniqueTogether(
            name='user_gym',
            unique_together={('user', 'gym')},
        ),
    ]
