from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bibliotecarios
from django.shortcuts import redirect
from hashlib import sha256


def loginB(request):
    status = request.GET.get('status')
    return render(request, 'loginB.html', {'status': status})

def cadastroB(request):
    status = request.GET.get('status')
    return render(request, 'cadastroB.html', {'status': status})
    #return HttpResponse('cadastro')

def valida_cadastroB(request):
    nome = request.POST.get('nome')
    cpf_biblio = request.POST.get('cpf_biblio')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    bibliotecario = Bibliotecarios.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(cpf_biblio.strip()) == 0:
        return redirect('/authB/cadastroB/?status=1')
    if len(senha) < 8:
        return redirect('/authB/cadastroB/?status=2')
    if len(bibliotecario) > 0:
        return redirect('/authB/cadastroB/?status=3')
    n = nome.strip()
    if len(nome.strip()) < 2 or n.isnumeric():
        return redirect('/authB/cadastroB/?status=5')
    s = senha.strip()
    tem_n = True
    tem_l = True
    for i in s:
      if not i.isnumeric():
        tem_n = False
      if not i.isalpha():
        tem_l = False
    if tem_n == False and tem_l == False:
        return redirect('/authB/cadastroB/?status=6')
    try:
        senha = sha256(senha.encode()).hexdigest()
        bibliotecario = Bibliotecarios(nome = nome, email = email, cpf_biblio = cpf_biblio, senha = senha)
        bibliotecario.save()

        return redirect('/authB/cadastroB/?status=0')
    except:
        return redirect('/authB/cadastroB/?status=4')
    
def valida_loginB(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    bibliotecario = Bibliotecarios.objects.filter(email = email).filter(senha = senha)

    if len(bibliotecario) == 0:
        return redirect('/authB/loginB/?status=1')
    elif len(bibliotecario) > 0:
        request.session['bibliotecario'] = bibliotecario[0].id
        return redirect('/sistema/home2/')


    return HttpResponse(f'{email} {senha}')

def sairB(request):
    request.session.flush()
    return redirect('/authB/loginB/')