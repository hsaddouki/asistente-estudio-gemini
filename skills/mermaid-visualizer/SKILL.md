---
name: mermaid-visualizer
description: Generador de diagramas Mermaid para visualización de arquitecturas de IA. Úsalo para convertir descripciones textuales de redes neuronales (Transformers, ResNets, UNets) en diagramas de flujo de datos y diagramas de secuencia.
---

# Mermaid Visualizer (Architecture-to-Diagram)

Esta skill permite aterrizar la complejidad de las arquitecturas del máster en representaciones visuales claras. Convierte bloques de ecuaciones y texto en diagramas estructurados.

## Flujos de Trabajo Principales

### 1. Visualización de Arquitecturas
Cuando expliques una arquitectura compleja (ej: Bloque de Attention, ResNet stage, UNet Bottleneck):
- **Acción:** Genera un bloque de código `mermaid` detallado.
- **Formato:** Utiliza `graph TD` para flujos de datos o `sequenceDiagram` para interacciones temporales (ej: procesos de difusión).
- **Detalle:** Incluye los `shapes` de los tensores en las conexiones entre nodos (cumpliendo con el Formats Hook).
