# Generated by Django 4.1.1 on 2022-11-28 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0007_livros_emprestado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='emprestado',
        ),
    ]
