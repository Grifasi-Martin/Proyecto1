from django.urls import path
from MarketCons.views import *

urlpatterns = [
    path('inicio/', inicio, name= "Inicio"),
    path('cliente/', cliente, name= "Cliente"),
    path('producto/', producto, name= "Producto"),
    path('ayuda/', ayuda, name= "Ayuda"),
    path('empleado/', empleado, name= "Empleado"),
    path('setCliente/', setCliente, name="setCliente"),
    path('getCliente/', getCliente, name="getCliente"),
    path('buscarCliente/', buscarCliente, name="buscarCliente"),
]