# Generated by Django 4.1.1 on 2023-01-24 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0018_livros_emprestado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='emprestado',
        ),
    ]
