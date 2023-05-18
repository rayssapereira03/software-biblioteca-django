from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from livro.models import Emprestimo
from django.shortcuts import redirect
from hashlib import sha256

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})
    #return HttpResponse('cadastro')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    email = request.POST.get('email')
    categoria = request.POST.get('categoria')
    #codigo = request.POST.get('código')
    turma = request.POST.get('turma')
    telefone = request.POST.get('telefone')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(turma.strip()) == 0 or len(telefone.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')
    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    n = nome.strip()
    if len(nome.strip()) < 2 or n.isnumeric():
        return redirect('/auth/cadastro/?status=5')
    s = senha.strip()
    tem_n = True
    tem_l = True
    for i in s:
      if not i.isnumeric():
        tem_n = False
      if not i.isalpha():
        tem_l = False
    if tem_n == False and tem_l == False:
        return redirect('/auth/cadastro/?status=6')
    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, email = email, categoria = categoria, turma = turma, telefone = telefone, senha = senha)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')
    
