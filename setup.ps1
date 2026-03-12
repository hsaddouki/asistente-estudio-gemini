# 🎓 Iniciando Configuración del Asistente de Estudio de Élite... (PowerShell)

$envFile = ".env"

if (Test-Path $envFile) {
    $overwrite = Read-Host "⚠️ El archivo .env ya existe. ¿Deseas sobreescribirlo? (s/n)"
    if ($overwrite -ne "s") {
        Write-Host "Configuración cancelada."
        exit
    }
}

# Solicitar Datos al Usuario
$vaultPath = Read-Host "📍 Introduce la RUTA ABSOLUTA de tu Bóveda de Obsidian (Ej: D:\Obsidian\Hamza)"
$courseName = Read-Host "📚 Introduce el nombre de la carpeta raíz en Obsidian (Ej: Master_IA)"
$rootTag = Read-Host "🏷️ Introduce la etiqueta raíz para tus asignaturas (Ej: Inteligencia Artificial)"

# Crear el contenido del archivo .env
$date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$envContent = @"
# Configuración Generada el $date
VAULT_PATH=$vaultPath
COURSE_NAME=$courseName
ROOT_TAG=$rootTag
STUDY_LANGUAGE=es
"@

# Guardar el archivo .env con codificación UTF8 sin BOM para compatibilidad
$envContent | Out-File -FilePath $envFile -Encoding utf8

Write-Host "`n✅ Archivo .env configurado correctamente." -ForegroundColor Green
Write-Host "🚀 Configuración guardada:"
Write-Host "   - Vault: $vaultPath"
Write-Host "   - Carpeta: $courseName"
Write-Host "   - Etiqueta Raíz: $rootTag"
