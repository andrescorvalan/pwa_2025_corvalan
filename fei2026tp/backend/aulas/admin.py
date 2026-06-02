from django.contrib import admin
from .models import Carrera, Profesor

admin.site.register(Carrera)  # <--- Registrar el modelo Carrera para que aparezca en el admin
admin.site.register(Profesor)  # <--- Registrar el modelo Profesor para que aparezca en el admin