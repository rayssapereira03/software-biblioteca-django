from django.contrib import admin
from reserva.models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_reserva','data_retirada','titulo','cod_leitor','cpf_biblio')