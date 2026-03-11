# Formats Hook: "Strict LaTeX & Tensors"

**Objetivo:** Garantizar una salida visual profesional y técnicamente rigurosa, evitando fórmulas en texto plano y asegurando la trazabilidad de dimensiones en código.

**Instrucción Obligatoria:**
"Intercepta cualquier expresión matemática. Prohibido el uso de texto plano para fórmulas. Usa obligatoriamente LaTeX $$...$$. En bloques de código de PyTorch/JAX, es obligatorio incluir un comentario con el shape de los tensores clave en cada línea de transformación."

**Ejemplo de Código:**
```python
x = self.conv(x)  # [Batch, 64, 28, 28]
```
