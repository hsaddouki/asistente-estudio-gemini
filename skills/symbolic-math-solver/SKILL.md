---
name: symbolic-math-solver
description: Solucionador simbólico para álgebra compleja y cálculo en IA. Úsalo para derivaciones formales de Backpropagation, simplificación de expresiones de teoría de la información (Entropía, Divergencia KL) y resolución de derivadas parciales pesadas.
---

# Symbolic Math Solver (SymPy/Wolfram)

Gemini es excepcional razonando, pero el álgebra pesada requiere determinismo. Esta skill utiliza `SymPy` para asegurar que las derivaciones matemáticas del máster sean 100% precisas.

## Flujos de Trabajo Principales

### 1. Derivaciones de Backpropagation
Cuando necesites la derivada de una función de activación custom o un optimizador:
- **Acción:** Define la expresión en `SymPy` y realiza la diferenciación simbólica.
- **Salida:** Expresión derivada en formato $\LaTeX$ y código Python ejecutable.

### 2. Teoría de la Información y Probabilidad
Simplificación de términos complejos como:
- Divergencia de Kullback-Leibler ($D_{KL}(P || Q)$).
- Entropía Cruzada y Log-Likelihood.
- Estimación de gradientes en modelos estocásticos.

### 3. Verificación Algebraica
Usa el script `scripts/symbolic_utility.py` para verificar si dos expresiones matemáticas son equivalentes, evitando errores de notación entre diferentes PDFs.

## Instrucción Crítica
"Para cualquier derivación formal que involucre más de dos pasos algebraicos, utiliza siempre una validación simbólica con esta skill antes de presentar el resultado final".

## Ejemplo de Uso
"Deriva formalmente la función de actualización para este optimizador custom basado en el gradiente de la pérdida de Huber".
