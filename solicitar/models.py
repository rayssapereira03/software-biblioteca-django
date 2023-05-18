from django.db import models

class Solicitar(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.titulo