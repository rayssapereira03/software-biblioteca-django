from django.db import models

class Busca(models.Model):
    editora_titulo_autor = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.editora_titulo_autor
