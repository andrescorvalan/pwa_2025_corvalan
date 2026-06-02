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
    

class ReservaAula(models.Model):
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='reservas')
    fh_desde = models.DateTimeField(null=False)
    fh_hasta = models.DateTimeField(null=False)
    observacion = models.CharField(max_length=256, null=True, blank=True) # Se asume opcional, si el profe la quiere obligatoria sacale el null/blank

    class Meta:
        # Nombre de la tabla en postgress, para respetar el enunciado y mas claridad en el nombre de tabla.
        # Sino django crearia aulas_reservaaula
        db_table = 'aulas_reserva_aula'

    def __str__(self):
        return f"Reserva {self.id} - Aula {self.id_aula.descripcion}"


class HorarioMateria(models.Model):
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='horarios')
    id_reserva = models.ForeignKey(ReservaAula, on_delete=models.CASCADE, related_name='horarios')
    fh_desde = models.DateTimeField(null=False)
    fh_hasta = models.DateTimeField(null=False)

    class Meta:
        # Nombre de la tabla en postgress, para respetar el enunciado y mas claridad en el nombre de tabla.
        # Sino django crearia aulas_reservaaula
        db_table = 'aulas_horario_materia'

    def __str__(self):
        return f"Horario {self.id} - Materia {self.id_materia.nombre}"