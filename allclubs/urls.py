from django.urls import path, include
from allclubs import views

urlpatterns = [
    path('', views.Inicio),
    path('Clubs', views.Clubs, name="Clubs"),
    path('Entrenadores', views.Entrenadores),
    path('Deportistas', views.Deportistas),
    path('Equipamiento', views.Equipamiento),    
]