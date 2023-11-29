from django.http import HttpResponse
from django.shortcuts import render
from .forms import crearCita
from .models import Medicos, Mascotas, Citas, Duenios

# Create your views here.

def index(request):
    mascotas = Mascotas.objects.all()
    medicos = Medicos.objects.all()
    if request.method == 'POST':
       Citas.objects.create(fecha=request.POST['fecha'], hora=request.POST['hora'], mascota_id=request.POST['mascota'], medico_id=request.POST['medico'])
    return render(request, 'index.html', {
        'title': 'Ajendar Cita',
        'form': crearCita,
        'mascotas': mascotas,
        'medicos': medicos
    })

def citas(request):
    mascotas = Mascotas.objects.all()
    medicos = Medicos.objects.all()
    citas = Citas.objects.all()
    duenios = Duenios.objects.all()
    return render(request, 'citas.html', {
        'title': 'Citas Ajendadas',
        'mascotas': mascotas,
        'medicos': medicos,
        'citas': citas,
        'duenios': duenios
    })