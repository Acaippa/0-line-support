# Generated by Django 4.0 on 2023-01-30 09:00

from django.db import migrations, models
import django.db.models.deletion
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_problem_dato_postet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategori',
            name='under_kategori',
        ),
        migrations.AddField(
            model_name='problem',
            name='under_kategori',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='pages.underkategori'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_id',
            field=models.IntegerField(default=pages.models.generate_id, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tittel',
            field=models.CharField(max_length=200),
        ),
    ]