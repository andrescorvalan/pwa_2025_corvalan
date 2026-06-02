from django.urls import path
from .views import CarreraMixin, ProfesorMixinDetail

urlpatterns = [
    # Ruta para Carreras: maneja el GET (listar) y el POST (crear)
    path('carreras/', CarreraMixin.as_view(), name='carrera-list-create'),
    path('profesores/<int:pk>/', ProfesorMixinDetail.as_view(), name='profesor-detail'),
]