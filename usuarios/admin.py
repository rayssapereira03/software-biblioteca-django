from django.contrib import admin
from usuarios.models import Usuario

admin.site.register(Usuario)
'''@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome','email','categoria','turma','telefone','senha')'''