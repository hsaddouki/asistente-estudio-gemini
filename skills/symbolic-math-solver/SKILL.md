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
