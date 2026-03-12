---
name: obsidian-sync
description: Sincronización automática de bloques de estudio con Obsidian siguiendo un sistema de etiquetas jerárquicas y organización por carpetas de asignatura.
---

# Obsidian Sync (Hierarchical Study Notes)

Esta skill transforma la salida técnica en notas de Obsidian con un sistema de etiquetado estructurado que permite la navegación por unidades y asignaturas.

## Formato de Nota
```markdown
[Titulo del Bloque]
Tags: [[Unidad X - Asignatura]]
---
Contenido (Markdown + LaTeX)
```

## Sistema de Etiquetas (Carpeta '3 - Etiquetas')
La skill asegura que existan los archivos de etiqueta con su jerarquía:
1. **Asignatura**: `[[Inteligencia Artificial]]` es su padre.
2. **Unidad**: `[[Asignatura]]` es su padre.

## Uso del Comando
```bash
python scripts/obsidian_saver.py --vault "RUTA" --unit_num "X" --subject "Asignatura" --block "Nombre" --content "MD"
```
