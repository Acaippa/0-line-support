# Generated by Django 4.0 on 2023-02-08 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_alter_ticket_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='state',
            field=models.ForeignKey(blank=True, default='open', null=True, on_delete=django.db.models.deletion.CASCADE, to='problems.state'),
        ),
    ]
