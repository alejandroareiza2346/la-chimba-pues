#!/bin/bash

# Instalar dependencias de Python
python3 -m pip install -r requirements.txt

# Limpiar archivos estáticos existentes
rm -rf staticfiles/*

# Recopilar archivos estáticos
python3 manage.py collectstatic --noinput

# Copiar archivos estáticos al directorio staticfiles
cp -r static/assets/bootstrap staticfiles/assets/bootstrap
cp -r static/assets/DataTables staticfiles/assets/DataTables
cp -r static/assets/select2 staticfiles/assets/select2

# Crear directorios necesarios
mkdir -p media
mkdir -p staticfiles
