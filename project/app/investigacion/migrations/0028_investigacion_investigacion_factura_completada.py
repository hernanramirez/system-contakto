# Generated by Django 2.2.27 on 2022-08-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigacion', '0027_investigacion_ejecutivo_de_cuentas_asignado'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigacion',
            name='investigacion_factura_completada',
            field=models.BooleanField(default=False),
        ),
    ]
