from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from livro.models import Livros
from .models import Busca
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views import generic



def listaLivro(request):
    status = request.GET.get('status')
    return render(request, 'listaLivro.html', {'status': status})

def busca(request):
    status = request.GET.get('status')
    return render(request, 'busca.html', {'status': status})
    

def valida_busca(request):
    editora_titulo_autor = request.POST.get('editora_titulo_autor')
    editora = Livros.objects.filter(editora = editora_titulo_autor)
    autor = Livros.objects.filter(autor = editora_titulo_autor)
    titulo = Livros.objects.filter(titulo = editora_titulo_autor)

    if len(editora_titulo_autor.strip()) == 0:
        return redirect('/busca/busca/?status=1')
    editora_titulo_autor1 = editora_titulo_autor.strip()
    if len(editora_titulo_autor1) < 2:
        return redirect('/busca/busca/?status=2')
    if len(editora) == 0 and len(autor) == 0 and len(titulo) == 0:
        return redirect('/busca/busca/?status=4')
    try:
        busca = Busca(editora_titulo_autor = editora_titulo_autor)
        busca.save()
        if len(editora) != 0:
            livro = Livros.objects.filter(editora = editora_titulo_autor)
            return render(request, 'listaLivro.html', {'livro': livro})
        elif len(autor) != 0:
            livro = Livros.objects.filter(autor = editora_titulo_autor)
            return render(request, 'listaLivro.html', {'livro': livro})
        else:
            livro = Livros.objects.filter(titulo = editora_titulo_autor)
            return render(request, 'listaLivro.html', {'livro': livro})
        #return redirect('http://127.0.0.1:8000/busca/listaLivro/')
      
    except:
        return redirect('/busca/busca/?status=3')


