FROM python:3.12.2-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Actualizar repositorios e instalar dependencias del sistema necesarias
# Por ahora netcat porque se usa en el entrypoint
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip && pip install --upgrade setuptools

# Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copiar el script de inicialización y darle permisos de ejecución
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Crear un usuario comun, por defecto ids 1000 (sino pasarlos por parametros) y asignarlo a WORKDIR
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN groupadd -g ${GROUP_ID} appuser && \
    useradd -u ${USER_ID} -g appuser -ms /bin/bash appuser
RUN chown appuser:appuser /usr/src/app

# Cambiar al usuario creado
USER appuser

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]