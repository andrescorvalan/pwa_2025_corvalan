from rest_framework import serializers
from .models import Carrera, Profesor, Materia, Aula, ReservaAula, HorarioMateria

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'
        extra_kwargs = {    # Mensajes de error personalizados para validaciones de campos
            'nombre': {
                'error_messages': {
                    'blank': 'El nombre de la carrera no puede estar vacío.',
                    'required': 'El campo nombre es obligatorio.',
                    'max_length': 'El nombre no puede superar los 128 caracteres.'
                }
            }
        }

    def validate_nombre(self, value):
        if value:
            value = value.strip().title()   # Eliminar espacios al inicio y al final, y cada primera letra en mayuscula
            if len(value) < 3:              # Validación para asegurar que el nombre tenga al menos 3 caracteres
                raise serializers.ValidationError("El nombre de la carrera es demasiado corto (mínimo 3 caracteres).")
        return value


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'
        extra_kwargs = {    # Mensajes de error personalizados para validaciones de campos
            'nombre': {
                'error_messages': {
                    'blank': 'El nombre del profesor no puede estar vacío.',
                    'required': 'El campo nombre es obligatorio.',
                    'max_length': 'El nombre no puede superar los 128 caracteres.'
                }
            },
            'apellido': {
                'error_messages': {
                    'blank': 'El apellido del profesor no puede estar vacío.',
                    'required': 'El campo apellido es obligatorio.',
                    'max_length': 'El apellido no puede superar los 128 caracteres.'
                }
            },
            'mostrar': {
                'error_messages': {
                    'blank': 'El campo mostrar no puede estar vacío.',
                    'required': 'El campo mostrar es obligatorio.',
                    'max_length': 'El formato mostrar no puede superar los 256 caracteres.'
                }
            }
        }

    def validate_nombre(self, value):
        if value:
            return value.strip().title()   # Eliminar espacios al inicio y al final, y cada primera letra en mayuscula
        return value

    def validate_apellido(self, value):
        if value:
            return value.strip().title()   # Eliminar espacios al inicio y al final, y cada primera letra en mayuscula
        return value

    def validate_mostrar(self, value):
        if value:
            return value.strip()                # Eliminar espacios al inicio y al final
        return value


class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
        extra_kwargs = {    # Mensajes de error personalizados para validaciones de campos
            'nombre': {
                'error_messages': {
                    'blank': 'El nombre de la materia no puede estar vacío.',
                    'required': 'El campo nombre es obligatorio.',
                    'max_length': 'El nombre no puede superar los 128 caracteres.'
                }
            },
            'cant_alumnos': {
                'error_messages': {
                    'invalid': 'La cantidad de alumnos debe ser un número entero.',
                    'required': 'La cantidad de alumnos es obligatoria.'
                }
            }
        }

    def validate_nombre(self, value):
        if value:
            value = value.strip().title()   # Eliminar espacios al inicio y al final, y cada primera letra en mayuscula
            if len(value) < 3:              # Validación para asegurar que el nombre tenga al menos 3 caracteres
                raise serializers.ValidationError("El nombre de la materia es demasiado corto (mínimo 3 caracteres).")
        return value

    def validate_cant_alumnos(self, value):
        if value < 0:
            raise serializers.ValidationError("La cantidad de alumnos no puede ser un número negativo.")
        return value


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'
        extra_kwargs = {    # Mensajes de error personalizados para validaciones de campos
            'descripcion': {
                'error_messages': {
                    'blank': 'La descripción del aula es obligatoria.',
                    'required': 'El campo descripción es obligatorio.',
                    'max_length': 'La descripción no puede superar los 128 caracteres.'
                }
            },
            'ubicacion': {
                'error_messages': {
                    'blank': 'La ubicación del aula es obligatoria.',
                    'required': 'El campo ubicación es obligatorio.',
                    'max_length': 'La ubicación no puede superar los 128 caracteres.'
                }
            }
        }

    def validate_descripcion(self, value):
        if value:
            return value.strip().capitalize()   # Eliminar espacios al inicio y al final, y capitalizar la primera letra
        return value

    def validate_ubicacion(self, value):
        if value:
            return value.strip().upper()        # Eliminar espacios al inicio y al final, y pasa a mayuscula
        return value
    
    def validate_aforo(self, value):
        if value < 0:
            raise serializers.ValidationError("El aforo no puede ser un número negativo.")
        return value
    
    def validate_cant_proyector(self, value):
        if value < 0:
            raise serializers.ValidationError("La cantidad de proyectores no puede ser un número negativo.")
        return value
    
class ReservaAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAula
        fields = '__all__'
        extra_kwargs = {
            'fh_desde': {'error_messages': {'required': 'La fecha y hora de inicio es obligatoria.', 'invalid': 'Fecha/Hora de inicio inválida.'}},
            'fh_hasta': {'error_messages': {'required': 'La fecha y hora de fin es obligatoria.', 'invalid': 'Fecha/Hora de fin inválida.'}},
            'observacion': {'error_messages': {'max_length': 'La observación no puede superar los 256 caracteres.'}}
        }

    # Para validar cruzado campos de un mismo modelo (desde y hasta), DRF recomienda usar el método validate general
    def validate(self, attrs):
        fh_desde = attrs.get('fh_desde')
        fh_hasta = attrs.get('fh_hasta')
        
        if fh_desde and fh_hasta and fh_hasta <= fh_desde:
            raise serializers.ValidationError({
                'fh_hasta': 'La fecha/hora de fin no puede ser anterior o igual a la de inicio.'
            })
            
        if 'observacion' in attrs and attrs['observacion']:
            attrs['observacion'] = attrs['observacion'].strip()
            
        return attrs

class HorarioMateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioMateria
        fields = '__all__'
        extra_kwargs = {
            'fh_desde': {'error_messages': {'required': 'La fecha y hora de inicio de la clase es obligatoria.', 'invalid': 'Fecha/Hora de inicio inválida.'}},
            'fh_hasta': {'error_messages': {'required': 'La fecha y hora de fin de la clase es obligatoria.', 'invalid': 'Fecha/Hora de fin inválida.'}}
        }

    def validate(self, attrs):
        fh_desde = attrs.get('fh_desde')
        fh_hasta = attrs.get('fh_hasta')
        
        if fh_desde and fh_hasta and fh_hasta <= fh_desde:
            raise serializers.ValidationError({
                'fh_hasta': 'El fin del horario de la materia no puede ser anterior o igual al inicio.'
            })
        return attrs