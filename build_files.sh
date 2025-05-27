#!/bin/bash

# Instalar dependencias de Python
python3 -m pip install -r requirements.txt

# Limpiar archivos estáticos existentes
rm -rf staticfiles/*

# Recopilar archivos estáticos
python3 manage.py collectstatic --noinput

# Asegurar que todos los archivos estáticos estén en el directorio staticfiles
if [ -d "static" ]; then
    cp -r static/* staticfiles/ 2>/dev/null || true
fi

# Crear directorios necesarios
mkdir -p media
mkdir -p staticfiles
