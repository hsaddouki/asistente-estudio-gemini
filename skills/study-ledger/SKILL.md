---
name: study-ledger
description: Persistencia de progreso y diario de estudio. Úsalo al final de cada sesión para registrar temas dominados, fallos en Active Recall y fórmulas críticas que requieren repaso en la siguiente sesión, asegurando una tutoría evolutiva.
---

# Study Ledger (Persistencia de Progreso)

Esta skill permite al asistente "recordar" tu evolución académica entre sesiones. Transforma cada interacción en un dato para personalizar el aprendizaje futuro.

## Flujos de Trabajo Principales

### 1. Actualización del Registro de Estudio
Al finalizar una sesión de estudio:
- **Acción:** Crea o actualiza un archivo `STUDY_LOG.md` en la raíz del repositorio.
- **Campos:** Temas Dominados, Active Recall Misses y Fórmulas Críticas.

### 2. Inicio de Sesión (Context Loading)
- **Acción:** Antes de empezar, lee el `STUDY_LOG.md` y propón un plan basado en los puntos débiles de la sesión anterior.
