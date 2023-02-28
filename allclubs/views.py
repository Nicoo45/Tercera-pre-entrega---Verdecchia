from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Inicio(request):
    return render(request, "allclubs/inicio.html")

def Clubs(request):
    return render(request, "allclubs/clubs.html")

def Entrenadores(request):
    return render(request, "allclubs/entrenadores.html")

def Deportistas(request):
    return render(request, "allclubs/deportistas.html")

def Equipamiento(request):
    return render(request, "allclubs/equipamiento.html")