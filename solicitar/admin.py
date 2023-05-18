from django.contrib import admin
from solicitar.models import Solicitar

@admin.register(Solicitar)
class SolicitarAdmin(admin.ModelAdmin):
    readonly_fields = ('titulo','autor','editora')