from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from MarketCons.models import Cliente
from MarketCons.forms import formSetCliente

# Create your views here.

def inicio(request):
    return render(request, "MarketCons/inicio.html")

def cliente(request):
    return render(request, "MarketCons/cliente.html")

def producto(request):
    return render(request, "MarketCons/producto.html")

def ayuda(request):
    return render(request, "MarketCons/ayuda.html")

def empleado(request):
    return render(request, "MarketCons/empleado.html")

def setCliente(request):
    if request.method == 'POST':
        elFormulario = formSetCliente(request.POST)
        print(elFormulario)
        if elFormulario.is_valid:
            data = elFormulario.cleaned_data
            cliente = Cliente(usuario=data["usuario"],contra=data["contra"],nombre=data["nombre"],apellido=data["apellido"],email=data["email"])    
            cliente.save()
            return render(request,"MarketCons/inicio.html")    
    else:
        elFormulario = formSetCliente()
    return render(request, "MarketCons/setCliente.html", {"elFormulario":elFormulario})

def getCliente(request):
    return render(request, "MarketCons/getCliente.html")

def buscarCliente(request):
    if request.GET["usuario"]:
        usuario = request.GET["usuario"]
        clientes = Cliente.objects.filter(usuario = usuario)
        return render(request, "MarketCons/getCliente.html", {"clientes":clientes})
    else:
        respuesta = "No se enviaron datos"
    
    return HttpResponse(respuesta)