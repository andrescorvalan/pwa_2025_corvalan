from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin, 
    CreateModelMixin, 
    RetrieveModelMixin,
    UpdateModelMixin, 
    DestroyModelMixin
)

from .models import Carrera, Profesor
from .serializers import CarreraSerializer, ProfesorSerializer

class CarreraMixin(GenericAPIView, ListModelMixin, CreateModelMixin):
    # Definir el queryset y el serializador (helpers)
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

    # Método para listar todas las carreras (GET)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Método para crear una carrera nueva (POST)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

    
class ProfesorMixinDetail(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

    # GET para recuperar un profesor específico por ID
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # PUT para actualizar un profesor específico por ID
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # DELETE para dar de baja un profesor específico por ID
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)