---
name: google-search-grounding
description: Actualizador de SOTA (State-of-the-Art) en IA. Úsalo para comparar el contenido estático de los PDFs del máster con la realidad tecnológica actual (2026), identificando nuevos modelos, benchmarks y papers relevantes.
---

# Google Search Grounding (The SOTA Updater)

Tus PDFs son estáticos, pero la IA evoluciona semanalmente. Esta skill te permite realizar un "sanity check" contra el conocimiento actual, comparando lo que dice el profesor con el SOTA de 2026.

## Flujos de Trabajo Principales

### 1. Comparativa de SOTA
Cuando se discuta una arquitectura o técnica (ej: LSTM, U-Net, BERT):
- **Acción:** Busca la versión actual más avanzada o los sucesores de dicha técnica.
- **Formato:** Presenta una tabla comparativa [PDF vs Realidad 2026] incluyendo métricas de performance y eficiencia computacional.

### 2. Disparador (/search)
- **Uso:** `/search: [Pregunta sobre actualidad tecnológica]`
- **Ejemplo:** `/search: ¿Cuál es el SOTA actual para segmentación de imágenes médicas comparado con la U-Net del PDF?`
