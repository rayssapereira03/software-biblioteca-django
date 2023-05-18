from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    categoria = models.CharField(max_length=50)
    #codigo = models.CharField(max_length=5)
    turma = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    senha = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nome