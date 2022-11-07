from django.http import HttpResponse
from django.template import Template, Context, loader

from datetime import datetime

def dia_hoy(request, edad):
    hoy = datetime.now()
    edad = int(edad)
    anio = datetime.now().year - edad
    respuesta=f"hoy es {hoy} y tu anio de nacimiento es: {anio}"
    return HttpResponse(respuesta)


def vista_saludo(request):
    return HttpResponse("HOLA MUNDO")


def vista_plantilla(request):
    archivo = open("/Users/felipe/Documents/coder4470/17_django/ProyectoCoder/ProyectoCoder/templates/template.html")
    
    plantilla = Template(archivo.read())
    archivo.close()
    contexto = Context()
    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def lista_alumnos(request):
    # Creamos el diccionario de datos
    listado_alumnos = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante",  "Barbara Pino"]
    datos = {"tecnologia": "Python", "listado_alumnos": listado_alumnos} #acceso a diccionario por key

    plantilla = loader.get_template("listado_alumnos.html") #me trae ya el template al ingresar la direccion de carpeta template en DIR setting
    documento = plantilla.render(datos) #renderizado del template

    return HttpResponse(documento)