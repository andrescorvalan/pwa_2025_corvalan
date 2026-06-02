from django.urls import path
from .views import CarreraMixin

urlpatterns = [
    # Ruta para Carreras: maneja el GET (listar) y el POST (crear)
    path('carreras/', CarreraMixin.as_view(), name='carrera-list-create'),
]