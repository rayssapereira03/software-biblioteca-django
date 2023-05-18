from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from bibliotecario.models import Bibliotecarios

def home2(request):
  if request.session.get('bibliotecario'):
    bibliotecario = Bibliotecarios.objects.get(id = request.session['bibliotecario'])
    return render(request, 'tela.html',{'usuario': bibliotecario})
    #return HttpResponse(f'olá {bibliotecario}')
    #return redirect('/admin/')
  else:
    return redirect('/authB/loginB/?status=2')
  