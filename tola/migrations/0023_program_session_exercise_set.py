# Generated by Django 4.1.3 on 2022-12-05 13:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0022_program_session_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='program_session_exercise_set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('num_of_reps', models.IntegerField()),
                ('percent', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('program_session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tola.program_session_exercise')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
