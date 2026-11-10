# A.R.I.A. — Asistente (rescatada 6 nov 2026)

Chatbot de terminal con LLM local. El archivo original es `aria.py` (48 líneas).

## Cómo funciona
- Usa **Ollama** en local con el modelo **llama3** (sin API key, sin nube).
- Personalidad: asistente ejecutiva y de desarrollo; trata a Ángel de "señor", tono sofisticado, directo y leal.
- Guarda el historial completo de la conversación en memoria mientras está encendida.
- Se apaga escribiendo `salir`, `apagar` o `exit`.

## Cómo correrla
```powershell
# 1. Instalar Ollama (https://ollama.com) y descargar el modelo
ollama pull llama3

# 2. Instalar dependencias
pip install langchain-ollama langchain-core

# 3. Correr
python aria.py
```

## Nota
La carpeta `venv/` que venía junto al archivo NO se respalda: es el entorno virtual de Python, se regenera con `pip install`. Nunca va a GitHub.
