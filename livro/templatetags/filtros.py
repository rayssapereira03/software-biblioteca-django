from django import template
from datetime import date, datetime

register = template.Library()

@register.filter
def mostra_duracao(value1, value2):
    if all((isinstance(value1, datetime), isinstance(value2, date))):
        dias = (value1 - value2).days
        texto = 'Dias'
        if dias == 1:
            texto = 'Dia'
        if dias < 0:
            dias = 0

        return f"{dias} {texto}."
    else:
        return "Ainda não foi devolvido."
