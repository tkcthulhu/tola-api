# Generated by Django 4.1.3 on 2022-11-28 21:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0010_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Max',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('num_of_reps', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(99999)])),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tola.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
