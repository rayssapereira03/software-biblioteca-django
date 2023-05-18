from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuario
from .models import Livros
from livro.models import Emprestimo
from bibliotecario.models import Bibliotecarios
from .forms import CadastroLivro
from django.db.models import Q
from datetime import date, datetime, timedelta
from hashlib import sha256


def home(request):
  #if request.session.get('usuario'):
   # usuario = Usuario.objects.get(id = request.session['usuario'])
    livros = Livros.objects.all()
    form = CadastroLivro()
    return render(request, 'home.html', {'livros': livros, 'form': form})
    #return HttpResponse(f'olá {usuario}')
    #return redirect('/admin/')
  #else:
   # return redirect('/auth/login/?status=2')

def home_empre(request):
  livros_emprestados = Emprestimo.objects.all()
  id = 0
  for l in livros_emprestados:
    id = l.livro_id
  livros = Livros.objects.filter(id = id).filter(emprestado = True)
  form = CadastroLivro()
  return render(request, 'home_empre.html', {'livros': livros, 'form': form})

def ver_livros(request, id):
    livro = Livros.objects.get(id = id)
    #if request.session.get('usuario') == livro.usuario.id:
    #usuario = Usuario.objects.get(id = request.session['usuario'])
    emprestimos = Emprestimo.objects.filter(livro = livro)
    form = CadastroLivro()
    return render(request, 'ver_livro.html', {'livro': livro, 'emprestimos': emprestimos, 'form': form, 'id_livro': id})

def Cadastrar_livro(request):
  if request.method == 'POST':
    form = CadastroLivro(request.POST, request.FILES)
    #imagem = request.FILES.get('img')


    if form.is_valid():
      form.save()
      return HttpResponse('Livro salvo com sucesso!!')

    else:
      return HttpResponse('Dados inválidos')

def excluir_livro(request, id):
    livro = Livros.objects.get(id = id).delete()
    return redirect('/livro/home')

def emprestimo(request):
  if request.session.get('usuario'):
    usuario = Usuario.objects.filter(id = request.session['usuario'])
    status = request.GET.get('status')
    return render(request, 'emprestimo.html', {'status': status , 'usuario': usuario})
    #return HttpResponse('teste')
  else:
    return redirect('/livro/login/?status=2')


def valida_emprestimo(request):
  if request.method =='POST':
    cpf_biblio = request.POST.get('cpf_biblio')
    cod_livro = request.POST.get('cod_livro')
    cod_leitor = request.POST.get('cod_leitor')

    emprestimo = Emprestimo.objects.filter(livro_id = cod_livro)
    livro = Livros.objects.filter(id = cod_livro)
    livroemprestado = Livros.objects.filter(id = cod_livro).filter(emprestado = True)
    bibliotecario = Bibliotecarios.objects.filter(cpf_biblio=cpf_biblio)
    user = Emprestimo.objects.filter(nome_emprestado = cod_leitor).filter(data_devolucao = None).count()
    user_cat = Usuario.objects.filter(id = cod_leitor).filter(categoria = 'Aluno(a)')
    userEm = Usuario.objects.filter(id = cod_leitor)
    usuario = Usuario.objects.filter(id = request.session['usuario'])
    if len(cod_livro.strip()) == 0 or len(cpf_biblio.strip()) == 0 or len(cod_leitor.strip()) == 0:
        return redirect('/livro/emprestimo/?status=1')
    if len(livroemprestado) > 0:
        return redirect('/livro/emprestimo/?status=2')
    if len(cpf_biblio) != 11:
        return redirect('/reserva1/reserva/?status=3')
    cpfB = cpf_biblio.strip()
    codL = cod_livro.strip()
    if codL.isalpha() == True or cpfB.isalpha() == True:
        return redirect('/livro/emprestimo/?status=4')
    if len(bibliotecario) == 0 or len(livro) == 0:
        return redirect('/livro/emprestimo/?status=5')
    if len(user_cat) > 0 and user == 3:
      return redirect('/livro/emprestimo/?status=6')
    if usuario[0] != userEm[0]:
      return redirect('/livro/emprestimo/?status=8')
    try:
        dias = datetime.now()
        dias += timedelta(days = 15)
        emprestimo = Emprestimo(nome_emprestado_id = cod_leitor, cpf_biblio = cpf_biblio, livro_id = cod_livro)
        emprestimo.data_prevista_devolucao = dias
        emprestimo.save()
        livro = Livros.objects.get(id = cod_livro)
        livro.emprestado = True
        livro.save()
        return redirect('/livro/home_empre/')
    except:
        return redirect('/livro/emprestimo/?status=7')

def devolucao(request):
    status = request.GET.get('status')
    return render(request, 'devolucao.html', {'status': status})

def valida_devolucao(request):
  if request.method =='POST':
    cod_livro = request.POST.get('cod_livro')

    emprestimo = Emprestimo.objects.filter(livro_id = cod_livro)
    livros = Livros.objects.filter(id = cod_livro)
    if len(cod_livro.strip()) == 0:
      return redirect('/livro/devolucao/?status=1')
    if len(livros) == 0:
      return redirect('/livro/devolucao/?status=2')
    try:    
      emprestimo_devolver = Emprestimo.objects.get(Q(livro = cod_livro) & Q(data_devolucao = None))
      emprestimo_devolver.data_devolucao = datetime.now() 
      emprestimo_devolver.save()
      livro = Livros.objects.get(id = cod_livro)
      livro.emprestado = False
      livro.save()

      return redirect('/livro/devolucao/?status=0')
    except:
        return redirect('/livro/devolucao/?status=3')

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)
    if len(usuario) == 0:
        return redirect('/livro/login/?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/livro/emprestimo/')
    else:
        return redirect('/livro/login/?status=2')
    
    return HttpResponse(f'{email} {senha}')


