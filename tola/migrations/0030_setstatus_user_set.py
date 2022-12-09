# Generated by Django 4.1.3 on 2022-12-07 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0029_program_session_exercise_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='user_set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('session_set', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tola.program_session_exercise_set')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tola.setstatus')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]