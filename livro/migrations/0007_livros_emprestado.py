# Generated by Django 4.1.1 on 2022-11-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0006_livros_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
    ]
