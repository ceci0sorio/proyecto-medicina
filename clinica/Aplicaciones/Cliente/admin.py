from django.contrib import admin
from .models import Paciente, Empleado, Consulta
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Empleado)
admin.site.register(Consulta)
