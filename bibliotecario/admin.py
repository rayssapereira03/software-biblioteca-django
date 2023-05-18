from django.contrib import admin
from bibliotecario.models import Bibliotecarios

@admin.register(Bibliotecarios)
class BibliotecariosAdmin(admin.ModelAdmin):
    readonly_fields = ('nome','email','cpf_biblio','senha')