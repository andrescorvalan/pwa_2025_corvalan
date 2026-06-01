#!/bin/bash

# Script para ejecutar comandos de Python dentro del contenedor 'django'
# "$@" pasa todos los argumentos recibidos directamente al comando python
docker compose exec django python "$@"