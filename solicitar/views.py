from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Solicitar
from livro.models import Livros
from django.shortcuts import redirect


def solicitar(request):
    status = request.GET.get('status')
    return render(request, 'solicitacao.html', {'status': status})


def valida_solicitar(request):
    titulo = request.POST.get('titulo')
    autor = request.POST.get('autor')
    editora = request.POST.get('editora')

    solicitar = Solicitar.objects.filter(titulo=titulo)
    livro = Livros.objects.filter(titulo=titulo)

    if len(titulo.strip()) == 0 or len(autor.strip()) == 0 or len(editora.strip()) == 0:
        return redirect('/solicitacao/solicitar/?status=1')
    if len(solicitar) > 0:
        return redirect('/solicitacao/solicitar/?status=2')
    if len(titulo.strip()) < 2 or len(autor.strip()) < 2 or len(editora.strip()) < 2:
        return redirect('/solicitacao/solicitar/?status=3')
    n = autor.strip()
    if n.isnumeric():
        return redirect('/solicitacao/solicitar/?status=4')
    if len(livro) > 0:
        return redirect('/solicitacao/solicitar/?status=6')
    try:
        solicitar = Solicitar(titulo = titulo, autor = autor, editora = editora)
        solicitar.save()
        return redirect('/solicitacao/solicitar/?status=0')
    except:
        return redirect('/solicitacao/solicitar/?status=5')
