# Generated by Django 4.1.1 on 2022-12-11 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='cpf_funcio',
            new_name='cpf_biblio',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 11, 17, 4, 1, 461078)),
        ),
    ]