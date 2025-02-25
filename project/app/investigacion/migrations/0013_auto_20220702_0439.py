# Generated by Django 2.2.27 on 2022-07-02 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigacion', '0012_investigacion_tipo_investigacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigacion',
            name='candidato_validado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='investigacion',
            name='entrevista_app_completado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='investigacion',
            name='entrevista_from_completado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='investigacion',
            name='laboral',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='investigacion',
            name='laboral_completado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='investigacion',
            name='psicometrico',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='investigacion',
            name='psicometrico_completado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='investigacion',
            name='entrevista',
            field=models.BooleanField(default=False),
        ),
    ]
