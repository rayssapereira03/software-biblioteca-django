# Generated by Django 4.1.1 on 2023-01-24 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0026_alter_reserva_data_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 24, 9, 26, 22, 629674)),
        ),
    ]
