from django.urls import path, include
from allclubs import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('clubs', views.clubs, name="clubs"),
    path('entrenadores', views.entrenadores, name="entrenadores"),
    path('deportistas', views.deportistas, name="deportistas"),
    path('equipamiento', views.equipamiento, name="equipamiento"),
    #path('ClubsFormulario', views.ClubsFormulario, name="ClubsFormulario"),
    #path('EntrenadoresFormulario', views.EntrenadoresFormulario, name="EntrenadoresFormulario"),    
]