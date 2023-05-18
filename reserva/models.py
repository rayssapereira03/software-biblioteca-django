from django.db import models
from datetime import date
import datetime

class Reserva(models.Model):
    data_reserva = models.DateTimeField(default=datetime.datetime.now())
    data_retirada = models.DateTimeField(blank = True, null = True)
    titulo = models.CharField(max_length=100)
    cod_leitor = models.CharField(max_length=5)
    cpf_biblio = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.titulo
