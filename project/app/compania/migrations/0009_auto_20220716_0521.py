# Generated by Django 2.2.27 on 2022-07-16 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compania', '0008_auto_20220716_0417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direccionfiscal',
            old_name='rcf',
            new_name='rfc',
        ),
        migrations.RemoveField(
            model_name='direccionfiscal',
            name='email',
        ),
    ]
