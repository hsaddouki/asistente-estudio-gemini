# 🎓 Asistente de Estudio de IA (2M Token Architecture)

Este repositorio constituye un **Entorno de Aprendizaje Dinámico** diseñado para explotar la ventana de contexto masiva de Gemini. No es un sistema RAG tradicional; es un **Sintetizador Académico** que procesa la bibliografía completa del Máster de forma holística.

## 🚀 Propósito
Facilitar el estudio profundo, la resolución de dudas técnicas y la generación de exámenes de práctica mediante una red de agentes especializados que operan sobre el material original de las asignaturas.

## 🏗️ Estructura del Ecosistema

| Directorio | Función |
| :--- | :--- |
| `/data` | **SSOT (Single Source of Truth)**. Contiene los PDFs originales (Ignorados por Git). |
| `/agents` | Definiciones de personalidad y protocolos (Math Prover, Code Architect, etc.). |
| `/hooks` | Interceptores de comportamiento para asegurar rigor técnico (LaTeX, Tensores). |
| `/skills` | Capacidades extendidas (Visualización de tensores, Exportador de Flashcards). |
| `/exam` | Repositorio de simulacros y evaluaciones generadas. |

## 🧠 Operativa de Agentes
El sistema utiliza un **Protocolo de Auto-Enrutamiento** que selecciona el agente óptimo según la consulta:
- **Math Prover**: Derivaciones y lógica formal.
- **Code Architect**: Implementaciones en PyTorch/JAX y optimización.
- **Synthesizer**: Resúmenes y mapas conceptuales globales.
- **Research Critic**: Análisis de papers SOTA y comparativas.

## 🛠️ Configuración Local
Para mantener el repositorio ligero, el contenido de `/data`, `/curriculum` y `/exam` está excluido del control de versiones. Gemini CLI puede leer estos directorios para proporcionar respuestas basadas en el contexto del máster.

> **Nota:** Este proyecto se rige por las directrices de `GEMINI.md`, priorizando la precisión técnica y la citación obligatoria de fuentes.
