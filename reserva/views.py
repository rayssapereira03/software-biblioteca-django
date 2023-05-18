from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva
from livro.models import Livros, Emprestimo
from usuarios.models import Usuario
from bibliotecario.models import Bibliotecarios
from django.shortcuts import redirect


def reserva(request):
    status = request.GET.get('status')
    return render(request, 'reservar.html', {'status': status})


def valida_reserva(request):
    data_reserva = request.POST.get('data_reserva')
    data_retirada = request.POST.get('data_retirada')
    titulo = request.POST.get('titulo')
    cod_leitor = request.POST.get('cod_leitor')
    cpf_biblio = request.POST.get('cpf_biblio')

    if cod_leitor != '' and cod_leitor.isnumeric() == True:
        s = int(cod_leitor)
    else:
        s = 0
    reserva = Reserva.objects.filter(titulo=titulo)
    reserva2 = Reserva.objects.filter(cod_leitor=cod_leitor)
    livro = Livros.objects.filter(titulo=titulo)
    user = Usuario.objects.filter(id=s)
    #user = usuario[0].id
    bibliotecario = Bibliotecarios.objects.filter(cpf_biblio=cpf_biblio)
    livro_empre = Livros.objects.filter(titulo = titulo).filter(emprestado = True)

    if len(titulo.strip()) == 0 or len(cod_leitor.strip()) == 0 or len(cpf_biblio.strip()) == 0:
        return redirect('/reserva1/reserva/?status=1')
    if len(reserva) > 0:
        return redirect('/reserva1/reserva/?status=2')
    if len(titulo) < 2 or len(cpf_biblio) != 11:
        return redirect('/reserva1/reserva/?status=3')
    codL = cod_leitor.strip()
    cpfB = cpf_biblio.strip()
    if codL.isalpha() == True or cpfB.isalpha() == True:
        return redirect('/reserva1/reserva/?status=4')
    if len(user) == 0 or len(bibliotecario) == 0 or len(livro) == 0:
        return redirect('/reserva1/reserva/?status=5')
    if len(reserva2) > 0:
        return redirect('/reserva1/reserva/?status=7') 
    if len(livro_empre) == 0:
        return redirect('/reserva1/reserva/?status=8')
    try:
        id = 0
        for l in livro_empre:
            id = l.id
        data_d_devolucao = Emprestimo.objects.filter(livro_id = id).filter(data_devolucao = None)
        data = str()
        for d in data_d_devolucao:
            data = d.data_prevista_devolucao
        reserva = Reserva(data_retirada=data, titulo=titulo, cod_leitor=cod_leitor, cpf_biblio=cpf_biblio)
        reserva.save()
        data_f = data.strftime('%d/%m/%Y')
        return HttpResponse(f'Reserva realizada com sucesso! Data de retira prevista para {data_f}')
        #return redirect('/reserva1/reserva/?status=0')
    except:
        return redirect('/reserva1/reserva/?status=6')
