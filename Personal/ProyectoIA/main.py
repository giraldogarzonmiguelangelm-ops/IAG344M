from flask import Flask, render_template, request, jsonify, session
from chatbot.model import predict_answer
import os

app = Flask(__name__)

# IMPORTANTE: La secret_key permite que Flask guarde la memoria del chat en el navegador
app.secret_key = "ducati_passion_2026" 

@app.route("/")
def home():
    # Cada vez que el usuario refresca la página, la memoria se reinicia
    session["chat_history"] = [] 
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_text = request.form.get("message", "")
    
    if not user_text.strip():
        return jsonify({"response": "Por favor, cuéntame qué Ducati tienes en mente. 😊"})

    # 1. Recuperamos el historial de la sesión (si no existe, creamos una lista vacía)
    history = session.get("chat_history", [])

    # 2. Guardamos lo que el usuario acaba de escribir
    history.append({"role": "user", "content": user_text})

    # 3. Llamamos a Groq pasando TODO el historial acumulado
    # Asegúrate de que en tu model.py la función predict_answer ahora reciba 'history'
    response_text = predict_answer(history)

    # 4. Guardamos la respuesta del bot en el historial para que la recuerde después
    history.append({"role": "assistant", "content": response_text})

    # 5. Actualizamos la sesión con el nuevo historial (limitamos a los últimos 10 mensajes para no saturar)
    session["chat_history"] = history[-10:]
    
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)