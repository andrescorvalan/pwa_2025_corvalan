#!/bin/bash

# Frenar el script si algo falla, evitando loops infinitos invisibles
set -e

echo "Esperando a que la base de datos en $POSTGRES_HOST:$POSTGRES_PORT esté lista..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.5
done
echo "¡Base de datos conectada con éxito!"

# Crear el proyecto base si la carpeta montada está vacía 
if [ ! -f "manage.py" ]; then
    echo "No se detectó un proyecto Django existente. Creando un proyecto nuevo..."
    django-admin startproject config .
fi

# Realizar migraciones automáticas 
echo "Chequeando y aplicando migraciones..."
python manage.py makemigrations
python manage.py migrate --noinput

# Crear el Superusuario usando variables nativas de Django 
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ] && [ "$DJANGO_SUPERUSER_EMAIL" ]; then
    echo "Configurando superusuario administrativo..."
    python manage.py createsuperuser --noinput || echo "El superusuario ya existe o fue omitido."
fi

# Reemplaza el proceso de Bash por Django (Apagado limpio con Ctrl+C o docker compose stop)
echo "Arrancando el servidor de desarrollo de Django en el puerto 8000..."
exec python manage.py runserver 0.0.0.0:8000