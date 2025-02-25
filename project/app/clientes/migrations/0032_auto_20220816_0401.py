# Generated by Django 2.2.27 on 2022-08-16 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0031_delete_clientesolicitudfactura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientesolicitudcandidato',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Estado'),
        ),
        migrations.AlterField(
            model_name='clientesolicitudcandidato',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Municipio'),
        ),
    ]
