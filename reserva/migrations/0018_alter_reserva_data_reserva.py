# Generated by Django 4.1.1 on 2023-01-23 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0017_alter_reserva_data_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_reserva',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 23, 9, 58, 16, 911098)),
        ),
    ]
