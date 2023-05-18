from django.urls import path
from . import views

urlpatterns = [
  path('loginB/', views.loginB, name = 'loginB'),
  path('cadastroB/', views.cadastroB, name = 'cadastroB'),
  path('valida_cadastroB/', views.valida_cadastroB, name = 'valida_cadastroB'),
  path('valida_loginB/', views.valida_loginB, name = 'valida_loginB'),
  path('sairB/', views.sairB, name = 'sairB')
  
]