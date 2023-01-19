from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Libro, Prestamo, Lector, Autor
from django.shortcuts import get_object_or_404, render
from .forms import CrearLibro, CrearLector, CrearAutor

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World!!!</h1>")

def index(request):
    return render(request, "index.html")

def libros(request):
    #libros = list(Libro.objects.values())
    libros = Libro.objects.all()
    return render(request, "libros.html", {
        "libros" : libros
    })

def prestamos(request):
    #prestamos = list(Prestamo.objects.values())
    prestamos = Prestamo.objects.all()
    return render(request, "prestamos.html", {
        "prestamos" : prestamos
    })

def crear_libro(request):
    if request.method == "GET":
        return render(request, "crear_libro.html", 
            {"form": CrearLibro()}
        )
    else:
        Libro.objects.create(titulo=request.POST["titulo"],
            tipo=request.POST["tipo"],
            editorial=request.POST["editorial"],
            anio=request.POST["anio"])
        return redirect("libros")
    
def lectores(request):
    lectores = Lector.objects.all()
    return render(request, "lectores.html", {
        "lectores" : lectores
    })

def crear_lector(request):
    if request.method == "GET":
        return render(request, "crear_lector.html", 
            {"form": CrearLector()}
        )
    else:
        Lector.objects.create(nombre=request.POST["nombre"],
            direccion=request.POST["direccion"],
            telefono=request.POST["telefono"],
            fecha_nac=request.POST["fecha_nac"],
            estado=request.POST["estado"])
        return redirect("lectores")

def crear_autor(request):
    if request.method == "GET":
        return render(request, "crear_autor.html", 
            {"form": CrearAutor()}
        )
    else:
        Autor.objects.create(nombre=request.POST["nombre"],
            direccion=request.POST["direccion"],
            telefono=request.POST["telefono"],
            fecha_nac=request.POST["fecha_nac"],
            nacionalidad=request.POST["nacionalidad"])
        return redirect("autores")

def autores(request):
    autores = Autor.objects.all()
    return render(request, "autores.html", {
        "autores" : autores
    })

def busquedaLibro(request):
    return render(request, "busquedaLibro.html")

def buscar(request):
    if request.GET["titulo"]:
        titulo = request.GET["titulo"]
        libros = Libro.objects.filter(titulo__icontains=titulo)
        return render(request, "resultadosPorBusqueda.html", {"libros": libros, "titulo":titulo})
    else:
        respuesta ="No enviaste datos"
    return HttpResponse(respuesta)

