# Generated by Django 2.2.27 on 2023-06-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adjuntos', '0006_auto_20220309_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjuntos',
            name='adj40',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Currículum Vitae'),
        ),
        migrations.AddField(
            model_name='adjuntos',
            name='adj41',
            field=models.FileField(blank=True, null=True, upload_to='adj', verbose_name='Solicitud de empleo'),
        ),
    ]
