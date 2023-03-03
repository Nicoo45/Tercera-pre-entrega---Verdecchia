from django.http.request import QueryDict
from django.shortcuts import render , HttpResponse
from django.http import HttpResponse
from allclubs.models import Clubs, Entrenadores, Deportistas, Equipamiento
from allclubs.forms import ClubsFormulario, EntrenadoresFormulario, DeportistasFormulario, EquipamientoFormulario

# Create your views here.

def inicio(request):
    return render(request, "allclubs/inicio.html")

#def clubs(request):
#   return render(request, "allclubs/clubs.html")

#def entrenadores(request):
#    return render(request, "allclubs/entrenadores.html")

#def deportistas(request):
#    return render(request, "allclubs/deportistas.html")

#def equipamiento(request):
#    return render(request, "allclubs/equipamiento.html")
"""
def clubsFormulario(request):
     return render(request, "allclubs/clubsFormulario.html")

def buscar(request):
    if request.GET["clubs"]:

        #mensaje = "Club buscado: %r" %request.GET["clubs"]
        clubes=request.GET["clubs"]
        clubs =Clubs.objects.filter(nombre__icontains=clubes)

        return render(request, "allclubs/resultados_busqueda.html", {"clubs": clubs, "query":clubes})

    else:

        mensaje= "No has introducido nada"

    return HttpResponse(mensaje)
"""
def clubs(request):
    if request.method== "POST":

        miFormulario= ClubsFormulario(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

            clubes = Clubs(nombre=infForm['clubs'], sede=infForm['sede'])

            clubes.save()

            return render(request, "allclubs/inicio.html")
        
    else: 

        miFormulario = ClubsFormulario()

    return render(request, "allclubs/clubs.html", {"miFormulario":miFormulario})

def entrenadores(request):
    if request.method== "POST":

        miFormulario= EntrenadoresFormulario(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

            entrenadores = Entrenadores(nombre=infForm['nombre'], apellido=infForm['apellido'], email=infForm['email'], especialidad=infForm['especialidad'])

            entrenadores.save()

            return render(request, "allclubs/inicio.html")
        
    else: 

        miFormulario = EntrenadoresFormulario()

    return render(request, "allclubs/entrenadores.html", {"miFormulario":miFormulario})

def deportistas(request):
    if request.method== "POST":

        miFormulario= DeportistasFormulario(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

            deportistas = Deportistas(nombre=infForm['nombre'], apellido=infForm['apellido'], email=infForm['email'], posicion=infForm['posicion'], fechaingreso=infForm['fecha_ingreso'])

            deportistas.save()

            return render(request, "allclubs/inicio.html")
        
    else: 

        miFormulario = DeportistasFormulario()

    return render(request, "allclubs/deportistas.html", {"miFormulario":miFormulario})

def equipamiento(request):
    if request.method== "POST":

        miFormulario= EquipamientoFormulario(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

            equipamiento = Equipamiento(articulo=infForm['articulo'], serie=infForm['serie'], sede=infForm['sede'], fecha_ingreso=infForm['fecha_ingreso'], usando=infForm['usando'])

            equipamiento.save()

            return render(request, "allclubs/inicio.html")
        
    else: 

        miFormulario = EquipamientoFormulario()

    return render(request, "allclubs/equipamiento.html", {"miFormulario":miFormulario})