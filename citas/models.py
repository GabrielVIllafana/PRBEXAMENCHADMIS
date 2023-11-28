from django.db import models

# Create your models here.

class Medicos(models.Model):
    nombre = models.CharField(max_length=200)
    ap_pat = models.CharField(max_length=200)
    ap_mat = models.CharField(max_length=200)
    especialidad = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    
class Duenios(models.Model):
    nombre = models.CharField(max_length=200)
    ap_pat = models.CharField(max_length=200)
    ap_mat = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    telefono = models.IntegerField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    
class Mascotas(models.Model):
    nombre = models.CharField(max_length=200)
    especie = models.CharField(max_length=200)
    raza = models.CharField(max_length=200)
    duenio = models.ForeignKey(Duenios, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    
class Citas(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)







