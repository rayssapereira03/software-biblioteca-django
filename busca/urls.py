from django.urls import path
from . import views

urlpatterns = [
  path('busca/', views.busca, name = 'busca'),
  path('valida_busca/', views.valida_busca, name = 'valida_busca'),
  path('listaLivro/', views.listaLivro, name = 'listaLivro')
  #path('BuscaList/', views.BuscaList, name = 'BuscaList')

]