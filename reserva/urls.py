from django.urls import path
from . import views

urlpatterns = [
  path('reserva/', views.reserva, name = 'reserva'),
  path('valida_reserva/', views.valida_reserva, name = 'valida_reserva')

]