#!/bin/bash

echo "🎓 Iniciando Configuración del Asistente de Estudio de Élite..."

# Comprobar si existe .env
if [ -f .env ]; then
    echo "⚠️ El archivo .env ya existe. ¿Deseas sobreescribirlo? (s/n)"
    read overwrite
    if [ "$overwrite" != "s" ]; then
        echo "Configuración cancelada."
        exit 0
    fi
fi

# Solicitar Datos al Usuario
echo "📍 Introduce la RUTA ABSOLUTA de tu Bóveda de Obsidian (Ej: D:\Obsidian\Hamza):"
read vault_path

echo "📚 Introduce el nombre de la carpeta raíz en Obsidian (Ej: Master_IA):"
read course_name

echo "🏷️ Introduce la etiqueta raíz para tus asignaturas (Ej: Inteligencia Artificial):"
read root_tag

# Crear el archivo .env
cat <<EOF > .env
# Configuración Generada el $(date)
VAULT_PATH=$vault_path
COURSE_NAME=$course_name
ROOT_TAG=$root_tag
STUDY_LANGUAGE=es
EOF

echo "✅ Archivo .env configurado correctamente."
echo "🚀 Configuración guardada:"
echo "   - Vault: $vault_path"
echo "   - Carpeta: $course_name"
echo "   - Etiqueta Raíz: $root_tag"
