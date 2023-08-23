# Generated by Django 2.2.27 on 2022-07-30 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0025_clientesolicitudcandidato_completado'),
        ('investigacion', '0022_auto_20220712_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigacion',
            name='cliente_solicitud_candidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.ClienteSolicitudCandidato'),
        ),
    ]
