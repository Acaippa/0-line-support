# Generated by Django 4.0 on 2023-01-25 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_problem_dato_postet'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='dato_postet',
            field=models.DateField(default=datetime.date.today),
        ),
    ]