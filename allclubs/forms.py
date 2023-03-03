from django import forms

class ClubsFormulario(forms.Form):
    clubs = forms.CharField()
    sede = forms.CharField()

class EntrenadoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=50)

class DeportistasFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    posicion = forms.CharField(max_length=30)
    fecha_ingreso = forms.DateField()

class EquipamientoFormulario(forms.Form):
    articulo = forms.CharField(max_length=30)
    serie = forms.IntegerField()
    sede = forms.CharField(max_length=50)
    fecha_ingreso = forms.DateField()
    usando = forms.BooleanField()