from django.contrib import admin
from .models import Medicos, Duenios, Citas, Mascotas

# Register your models here.

admin.site.register(Medicos)
admin.site.register(Duenios)
admin.site.register(Citas)
admin.site.register(Mascotas)
