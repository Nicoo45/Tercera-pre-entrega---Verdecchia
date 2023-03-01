from django.urls import path, include
from allclubs import views

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('Clubs', views.Clubs, name="Clubs"),
    path('Entrenadores', views.Entrenadores, name="Entrenadores"),
    path('Deportistas', views.Deportistas, name="Deportistas"),
    path('Equipamiento', views.Equipamiento, name="Equipamiento"),    
]