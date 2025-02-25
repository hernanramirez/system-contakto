# Generated by Django 2.2.27 on 2022-06-24 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investigacion', '0010_auto_20220619_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestigacionBitacora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(default='', max_length=120)),
                ('observaciones', models.TextField(default='')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('investigacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investigacion.Investigacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
