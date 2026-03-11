---
name: flashcard-summary-exporter
description: Exportador de resúmenes y flashcards para Anki. Úsalo para automatizar la creación de materiales de estudio de largo plazo, convirtiendo conceptos complejos del máster en tarjetas de memoria (CSV/TSV) y resúmenes estructurados en `RESUMEN.md`.
---

# Flashcard & Summary Exporter (Long-Term Retention)

Esta skill permite que el aprendizaje del máster sea productivo a largo plazo mediante la generación automática de materiales para *Spaced Repetition* (Anki) y documentación técnica condensada.

## Flujos de Trabajo Principales

### 1. Generación de Flashcards para Anki
Cuando se discutan conceptos teóricos o fórmulas críticas:
- **Acción:** Genera un bloque de texto en formato CSV/TSV [Pregunta;Respuesta;Referencia].
- **Formato:** Sigue el estándar de Anki (campos separados por `;`). Incluye siempre la cita al PDF en la respuesta.
- **Disparador:** `/export-flashcards: [TEMA/PREGUNTA]`

### 2. Exportación de Resúmenes Estructurados
- **Acción:** Crea o actualiza un archivo `RESUMEN.md` con la síntesis del tema actual.
- **Formato:** Jerárquico, incluyendo las fórmulas en LaTeX y los diagramas Mermaid generados.

## Instrucción Crítica
"Al exportar flashcards, prioriza el Active Recall: diseña preguntas que requieran explicar el 'por qué' o deducir una consecuencia, no solo definiciones de una palabra".

## Ejemplo de Exportación (Anki)
`¿Por qué se prefiere el Gradiente Estocástico (SGD) sobre el Gradiente Descendente Batch?;Porque reduce el riesgo de quedar atrapado en mínimos locales y es computacionalmente más eficiente en datasets masivos;[Semana_2.pdf | pág. 12]`

## Ejemplo de Uso
"/export-flashcards: Crea 5 preguntas difíciles sobre el tema de Gradiente Estocástico".
