from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    apellido = models.CharField(max_length=128, null=False, blank=False)
    mostrar = models.CharField(max_length=256, null=False, blank=False)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Materia(models.Model):
    nombre = models.CharField(max_length=128, null=False, blank=False)
    cant_alumnos = models.IntegerField(default=5, null=False)
    # Clave foránea a la Tablas Carrera
    # Si se borra la carrera, se borran las materias asociadas (on_delete=models.CASCADE)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='materias')
    # Clave foránea a Profesor
    # Si se borra el profesr, se borran las materias asociadas (on_delete=models.CASCADE)
    # Si no se desea este comportamiento, se puede usar on_delete=models.SET_NULL y permitir null=True
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='materias')
    def __str__(self):
        return self.nombre

class Aula(models.Model):
    descripcion = models.CharField(max_length=128, null=False, blank=False)
    ubicacion = models.CharField(max_length=128, null=False, blank=False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)
    def __str__(self):
        return self.descripcion 