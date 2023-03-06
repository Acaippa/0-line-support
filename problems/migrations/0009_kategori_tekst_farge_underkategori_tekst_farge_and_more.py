# Generated by Django 4.0 on 2023-03-06 09:23

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0008_rename_state_status_remove_ticket_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='tekst_farge',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='underkategori',
            name='tekst_farge',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kategori',
            name='farge',
            field=colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='underkategori',
            name='farge',
            field=colorfield.fields.ColorField(default='#ffffff', image_field=None, max_length=18, samples=None),
        ),
    ]