# Generated by Django 2.2.27 on 2022-07-08 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_auto_20220707_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trayectorialaboral',
            old_name='fecha_solicitud',
            new_name='fecha_creacion',
        ),
    ]
