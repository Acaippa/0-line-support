# Generated by Django 4.0 on 2023-01-18 10:05

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_problem_problem_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='id',
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_id',
            field=models.IntegerField(default=pages.models.generate_id, editable=False),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tittel',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]