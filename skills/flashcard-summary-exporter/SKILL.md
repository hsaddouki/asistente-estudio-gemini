---
name: flashcard-summary-exporter
description: Exportador de resúmenes y flashcards para Anki. Úsalo para automatizar la creación de materiales de estudio de largo plazo, convirtiendo conceptos complejos del máster en tarjetas de memoria (CSV/TSV) y resúmenes estructurados en `RESUMEN.md`.
---

# Flashcard & Summary Exporter (Long-Term Retention)

Esta skill permite que el aprendizaje del máster sea productivo a largo plazo mediante la generación automática de materiales para *Spaced Repetition* (Anki) y documentación técnica condensada.

## Flujos de Trabajo Principales

### 1. Generación de Flashcards para Anki
- **Acción:** Genera un bloque de texto en formato CSV/TSV [Pregunta;Respuesta;Referencia].
- **Formato:** Sigue el estándar de Anki (campos separados por `;`).
- **Disparador:** `/export-flashcards: [TEMA/PREGUNTA]`

### 2. Exportación de Resúmenes Estructurados
- **Acción:** Crea o actualiza un archivo `RESUMEN.md` con la síntesis del tema actual.
- **Formato:** Jerárquico, incluyendo las fórmulas en LaTeX y los diagramas Mermaid generados.
