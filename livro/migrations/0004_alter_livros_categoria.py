# Generated by Django 4.1.1 on 2022-11-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_categoria_alter_livros_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='categoria',
            field=models.CharField(max_length=100),
        ),
    ]
