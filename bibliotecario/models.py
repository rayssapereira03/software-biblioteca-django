from django.db import models

class Bibliotecarios(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cpf_biblio = models.CharField(max_length=11)
    senha = models.CharField(max_length=8)

    class Meta:
        verbose_name = 'Bibliotecario'
  
    def __str__(self) -> str:
        return self.nome
