from django import forms

class crearCita(forms.Form):
    fecha = forms.DateField()
    hora = forms.TimeField()