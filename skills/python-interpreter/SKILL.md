---
name: python-interpreter
description: Intérprete de Python para validación técnica en IA. Úsalo para verificar dimensiones de tensores (PyTorch/JAX), graficar funciones de pérdida, probar multiplicaciones de matrices y evitar alucinaciones en cálculos matemáticos del máster.
---

# Python Interpreter (The Sandbox)

Esta skill permite aterrizar la teoría del máster en código ejecutable. Es la herramienta de "sanity check" definitiva para evitar alucinaciones en dimensiones de tensores y arquitecturas complejas.

## Flujos de Trabajo Principales

### 1. Validación de Tensores (PyTorch/JAX)
Cuando se discute una arquitectura (ej: Conv2D, Self-Attention), utiliza el intérprete para verificar que el paso de datos entre capas es coherente.
- **Entrada:** Dimensiones del input [B, C, H, W] y parámetros de la capa.
- **Acción:** Ejecuta una pasada de prueba con datos dummy.
- **Salida:** Confirmación de las dimensiones del output o reporte del error exacto de dimensión.

### 2. Derivaciones Matemáticas y Gráficas
Usa `numpy` y `matplotlib` para visualizar conceptos abstractos:
- Distribuciones de probabilidad (Gaussianas, Bernoulli).
- Superficies de pérdida ($L(\hat{y}, y)$).
- Comportamiento de gradientes.

### 3. Scripts de Referencia
La skill incluye `scripts/tensor_validator.py` para chequeos rápidos de compatibilidad.

## Restricciones
- Prioriza siempre las bibliotecas estándar del proyecto (PyTorch, JAX, NumPy).
- Todo código generado debe incluir comentarios de `shape` en cada línea crítica (cumpliendo con el Formats Hook).
- Si el código falla, reporta el `Traceback` y sugiere la corrección basada en la teoría del PDF.
