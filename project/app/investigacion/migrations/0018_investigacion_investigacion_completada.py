# Generated by Django 2.2.27 on 2022-07-11 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigacion', '0017_investigacion_psicometrico_ejecutivo_asignado'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigacion',
            name='investigacion_completada',
            field=models.BooleanField(default=False),
        ),
    ]
