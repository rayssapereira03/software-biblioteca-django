# Generated by Django 4.1.1 on 2022-11-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('categoria', models.CharField(max_length=50)),
                ('turma', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('senha', models.CharField(max_length=8)),
            ],
        ),
    ]
