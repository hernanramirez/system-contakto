# Generated by Django 2.2.27 on 2022-06-12 17:44

import app.clientes.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compania', '0003_auto_20220421_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('compania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compania.Compania')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteSolicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enviado', models.BooleanField(default=False)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_solicitud', to='clientes.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ClienteSolicitudCandidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=140)),
                ('apellido', models.CharField(default='', max_length=140)),
                ('nss', models.CharField(blank=True, max_length=30, null=True, validators=[app.clientes.models.validate_nss])),
                ('email', models.CharField(blank=True, max_length=140, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('curp', models.CharField(blank=True, max_length=30, null=True, validators=[app.clientes.models.validate_curp])),
                ('puesto', models.CharField(blank=True, max_length=140, null=True)),
                ('status', models.CharField(blank=True, choices=[('0', 'En Investigación'), ('1', 'Pdt. por Cliente'), ('2', 'Inv. Terminada')], default='0', max_length=140, null=True)),
                ('tipo_investigacion_status', models.IntegerField(blank=True, choices=[(1, 'Laboral'), (2, 'Socioeconómico'), (4, 'Psicometrías'), (5, 'Visita Domiciliaria'), (7, 'Visita Domiciliaria con demandas'), (6, 'Validación de Demandas'), (3, 'Otro')], null=True)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('cliente_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_solicitud_candidato', to='clientes.ClienteSolicitud')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Estado')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Municipio')),
            ],
        ),
    ]
