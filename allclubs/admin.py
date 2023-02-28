from django.contrib import admin
from .models import Clubs, Entrenadores, Deportistas, Equipamiento
# Register your models here.
admin.site.register(Clubs)
admin.site.register(Entrenadores)
admin.site.register(Deportistas)
admin.site.register(Equipamiento)