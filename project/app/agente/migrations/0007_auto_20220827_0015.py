# Generated by Django 2.2.27 on 2022-08-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agente', '0006_gestorinfo_tipo_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestorinfo',
            name='banco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='gestorinfo',
            name='clabe_interbancaraia',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
