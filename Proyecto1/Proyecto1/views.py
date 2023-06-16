from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Django - Equipo Coder")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1> Hola Mundo!</h1>")

def miNombreEs(self, nombre):
    data = f"Mi nombre es: <h1> {nombre}</h1>"
    return HttpResponse(data)

def probandoTemplate(self):
    nombre = "Martin"
    apellido = "Grifasi"

    namelist = ["Julieta", "Cecilia", "Francisco", "Antonella", "Felipe"]

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }

    #No se usa mas y se configuro en settings DIRS #miHtml = open("C:/Users/marti/OneDrive/Documents/Python/Proyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    #Se carga directamente ne plantilla #loader.get_template("template1.html")
    #Se deja de usar tecnologia template #plantilla = Template(miHtml.read())
    plantilla = loader.get_template("template1.html")
    #No se lee mas archivo #miHtml.close()
    #Se deja de usar tecnologia context se renderiza diccionario #miContext = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)