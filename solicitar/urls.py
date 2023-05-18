from django.urls import path
from . import views

urlpatterns = [
  path('solicitar/', views.solicitar, name = 'solicitar'),
  path('valida_solicitar/', views.valida_solicitar, name = 'valida_solicitar')

]