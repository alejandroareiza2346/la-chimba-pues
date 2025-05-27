#!/bin/bash

# Instalar dependencias
pip install -r requirements.txt

# Crear directorio staticfiles si no existe
mkdir -p staticfiles

# Recolectar archivos estáticos
python manage.py collectstatic --noinput
