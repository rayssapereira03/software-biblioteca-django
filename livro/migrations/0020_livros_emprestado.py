# Generated by Django 4.1.1 on 2023-01-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0019_remove_livros_emprestado'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
    ]
