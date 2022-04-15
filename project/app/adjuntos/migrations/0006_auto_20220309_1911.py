# Generated by Django 2.2.24 on 2022-03-10 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adjuntos', '0004_auto_20210601_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjuntos',
            name='adj10',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='3. Gestor Entrevistador'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj11',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='5. Aviso Privacidad'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj12',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='6. Constancia'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj13',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='4. Croquis'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj14',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='7.a Identificación con fotografia'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj16',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='9. Comprobante de domicilio'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj17',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='8. Acta de nacimiento'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj18',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Carta Laboral'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj19',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Adicionales A'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj2',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='1. Foto de perfil del candidato'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj20',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Adicionales B'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj21',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Adicionales C'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj22',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='7.b Identificación con fotografia'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj23',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='7.c Identificación con fotografia'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj24',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='7.d Identificación con fotografia'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj25',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='10.b Semanas Cotizadas'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj26',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='10.c Semanas Cotizadas'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj27',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='10.d Semanas Cotizadas'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj28',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='10.e Semanas Cotizadas'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj29',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Adicionales D'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj3',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='2.a Interior derecho'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj30',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Adicionales E'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj31',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Adicionales F'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj32',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Adicionales G'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj33',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Adicionales H'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj34',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Adicionales I'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj35',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Extra A'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj36',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='11.b Validacion web'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj37',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Carta Laboral Extra'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj4',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='2.b Interior izquierdo'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj5',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='2.c Exterior derecho'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj6',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='2.d Exterior izquierdo'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj7',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='11.a Validación de Demandas Laborales'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj8',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='10.a Semanas Cotizadas'),
        ),
        migrations.AlterField(
            model_name='adjuntos',
            name='adj9',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='2.e Frente'),
        ),
    ]
