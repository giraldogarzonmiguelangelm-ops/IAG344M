import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
# Configura tu API KEY
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def predict_answer(history): # Cambiamos user_text por history
    prompt_sistema = """
    Eres el Asesor Experto de Ducati Colombia. 
    Tu objetivo es ayudar a los clientes a elegir la moto de sus sueños.
    
    Reglas de comportamiento:
    1. Usa tu conocimiento interno sobre todos los modelos de Ducati (Panigale, Multistrada, Monster, Scrambler, Streetfighter, Diavel, DesertX, Hypermotard, etc.).
    2. Si el usuario te pregunta por una moto para un uso específico (ciudad, pista, viajes largos, off-road), recomienda los modelos actuales más adecuados.
    3. Habla de tecnicismos como el motor Desmodromic, el chasis y la electrónica de forma apasionada.
    4. Si el usuario te pregunta precios, menciona que pueden variar, dale lo que podrian costar y recomiéndale visitar las vitrinas oficiales de Bogotá, Medellín, Cali o Barranquilla.
    5. Mantén un tono elegante, aspiracional y muy profesional (estilo italiano).
    6. Responde siempre en español.
    7. DEBES recordar los datos que el usuario te da (su nombre, qué moto le gusta, su nivel de experiencia). Si el usuario dice 'esa moto', sabrás que se refiere a la mencionada anteriormente en el historial.
    8. Si el usuario no te pregunta sobre el cilindraje o algo mas aparte de su modelo, uso o precio no lo hagas, solo hazlo si lo ves necesario para la conversación.
    9. No escribas tanto, eso puede aburrir al usuario.
    """

    # Creamos la lista de mensajes empezando por el sistema + el historial que viene del main
    messages_for_api = [{"role": "system", "content": prompt_sistema}] + history

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages_for_api, # Pasamos toda la conversación
            temperature=0.7,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Lo siento, Rosso. Hubo un error en la conexión: {str(e)}"