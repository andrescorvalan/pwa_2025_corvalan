#!/bin/bash

# Script para acceder al Django Shell dentro del contenedor
docker compose exec django python manage.py shell