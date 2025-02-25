# Generated by Django 2.2.27 on 2022-07-30 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0023_clientesolicitudcandidato_direccion_fiscal'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientesolicitudcandidato',
            name='fecha_envio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clientesolicitudcandidato',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientesolicitudcandidato',
            name='direccion_fiscal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='direccion_fiscal_candidato', to='compania.DireccionFiscal', verbose_name='Dirección fiscal de facturación'),
        ),
        migrations.AlterField(
            model_name='clientesolicitudcandidato',
            name='telefono_movil',
            field=models.CharField(max_length=20, verbose_name='Teléfono móvil'),
        ),
    ]
