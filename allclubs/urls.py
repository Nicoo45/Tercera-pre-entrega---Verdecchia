from django.urls import path, include
from allclubs import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('clubs', views.clubs, name="clubs"),
    path('entrenadores', views.entrenadores, name="entrenadores"),
    path('deportistas', views.deportistas, name="deportistas"),
    path('equipamiento', views.equipamiento, name="equipamiento"),
    #path('buscar_clubs', views.buscar_clubs),
    #path('buscar/', views.buscar),
]