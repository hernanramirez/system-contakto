# Generated by Django 2.2.27 on 2022-07-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0024_auto_20220730_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientesolicitudcandidato',
            name='completado',
            field=models.BooleanField(default=False),
        ),
    ]
