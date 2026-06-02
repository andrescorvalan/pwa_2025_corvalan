from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Carrera
from .serializers import CarreraSerializer

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