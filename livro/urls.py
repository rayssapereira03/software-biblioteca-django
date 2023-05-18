from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name = 'home'),
  path('ver_livro/<int:id>', views.ver_livros, name='ver_livros'),
  path('Cadastrar_livro/', views.Cadastrar_livro, name='Cadastrar_livro'),
  path('excluir_livro/<int:id>', views.excluir_livro, name='excluir_livro'),
  path('emprestimo/', views.emprestimo, name = 'emprestimo'),
  path('valida_emprestimo/', views.valida_emprestimo, name = 'valida_emprestimo'),
  path('home_empre/', views.home_empre, name='home_empre'),
  path('devolucao/', views.devolucao, name = 'devolucao'),
  path('valida_devolucao/', views.valida_devolucao, name = 'valida_devolucao'),
  path('login/', views.login, name = 'login'),
  path('valida_login/', views.valida_login, name = 'valida_login')

]