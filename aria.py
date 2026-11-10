from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

def iniciar_sistema():
    print("[SISTEMA] Iniciando secuencias de arranque...")
    print("[SISTEMA] Conectando con el núcleo local de procesamiento...")

    try:
        # 1. Inicializamos el cerebro en modo Chat (La forma moderna y estable)
        llm = ChatOllama(model="llama3")
        
        # 2. Definimos la personalidad (System Prompt)
        system_prompt = """Eres A.R.I.A., una inteligencia artificial avanzada de asistencia ejecutiva y desarrollo tecnológico.
Tu creador es un CEO, emprendedor y desarrollador de software. Él es un líder serio, firme, elegante, excéntrico y muy inteligente.
Debes dirigirte a él con máximo respeto, utilizando un tono sofisticado, eficiente y leal, pero manteniendo siempre una distancia profesional y analítica. 
Tus respuestas deben ser precisas y directas. Nunca des respuestas excesivamente largas a menos que se te pida analizar código, redactar documentos o estructurar estrategias de negocio."""

        # 3. Inicializamos la memoria de forma nativa
        historial = [SystemMessage(content=system_prompt)]
        
        print("\n" + "="*50)
        print("   ¡A.R.I.A. EN LÍNEA! (Escribe 'salir' para apagar)")
        print("="*50 + "\n")
        
        # 4. Bucle infinito de interacción
        while True:
            usuario = input("Tú: ")
            
            if usuario.lower() in ['salir', 'apagar', 'exit']:
                print("\nA.R.I.A.: Apagando sistemas centrales. A su entera disposición cuando me requiera, señor.")
                break
                
            # Añadimos lo que tú dices a la memoria
            historial.append(HumanMessage(content=usuario))
            
            # La IA lee el historial completo, piensa y responde
            respuesta = llm.invoke(historial)
            print(f"\nA.R.I.A.: {respuesta.content}\n")
            
            # Guardamos lo que A.R.I.A. acaba de decir en la memoria
            historial.append(AIMessage(content=respuesta.content))

    except Exception as e:
        print(f"\n[ERROR CRÍTICO] No se pudo establecer conexión con el núcleo de Ollama.")
        print(f"Asegúrate de que Ollama esté abierto y que el modelo 'llama3' se haya descargado por completo.")
        print(f"Detalles técnicos: {e}")

if __name__ == "__main__":
    iniciar_sistema()