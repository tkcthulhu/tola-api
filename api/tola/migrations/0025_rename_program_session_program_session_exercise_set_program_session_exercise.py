# Generated by Django 4.1.3 on 2022-12-05 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tola', '0024_program_session_exercise_set_set_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program_session_exercise_set',
            old_name='program_session',
            new_name='program_session_exercise',
        ),
    ]