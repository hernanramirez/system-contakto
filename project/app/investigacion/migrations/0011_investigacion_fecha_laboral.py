# Generated by Django 2.2.27 on 2022-10-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigacion', '0010_auto_20220619_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigacion',
            name='fecha_laboral',
            field=models.DateField(blank=True, null=True),
        ),
    ]
