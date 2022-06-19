# Generated by Django 2.2.27 on 2022-06-12 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('efe_key', models.CharField(db_index=True, max_length=3, unique=True)),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_key', models.CharField(db_index=True, max_length=3, unique=True)),
                ('municipio', models.CharField(max_length=30)),
                ('efe_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estado')),
            ],
        ),
    ]
