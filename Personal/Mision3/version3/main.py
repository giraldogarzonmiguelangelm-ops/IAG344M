from flask import Flask, render_template, request, jsonify  #Importa la libreria de flask: Clase principal para crear la aplicación web, render_template: función que sirve para cargar archivos html desde mi carpeta templates, request: Objeto que representa la petición del usuario, permite acceder a formularios, headers, etc. jsonify:Convierte un diccionario de Python en respuesta JSON, ideal para APIs o chatbots.
from chatbot.data import training_data
from chatbot.model import build_and_train_model,predict_answer,load_model
app = Flask(__name__)    #Le decimos a flask donde debe buscar recursos como templates o archivos estáticos
model,vectorizer,unique_answers=load_model()   #Carga el modelo y devuelve esos tres
if model is None:         #Comprueba si no se pudo cargar un modelo existente
        model,vectorizer,unique_answers=build_and_train_model(training_data)   #Si no existe entrena un modelo nuevo con los datos del training_data
@app.route("/")    #Define la ruta principal de la web
def home():        #Función que se ejecuta cuando alguien entra en la página
        return render_template("index.html")   #Carga el archivo index.html desde la carpeta templates
@app.route("/chat",methods=["POST"])   #Define la ruta donde el chat recibe los mensajes
def chat():           #Función que maneja la conversación
        user_text = request.form.get("message","")   #Obtiene el mensaje del usuario, buscandolo en el campo llamado message, y si no encuentra nada devuelve cadena vacía
        if not user_text.strip():      #Verifica si el usuario envio espacios en blanco, elimina los espacios al inicio y al fin, 
                return jsonify({"response":"Por Favor escribe algo 😊"})        #Si el espacio esta vacío devuelve un JSON con la respuesta
        response =predict_answer(model,vectorizer,unique_answers,user_text)   #Llama a la función predict_answer, para obtener la respuesta del bot y lo guarda en response
        return jsonify({"response":response})      #Envia la respuesta que recibimos en el fetch de nuestros scripts en formato JSON al navegador
if __name__ == "__main__":                #Comprueba si el archivo se está ejecutando directamente
    app.run(host="0.0.0.0",port=5000)  #Inicia el servidor flask,(host="0.0.0.0", port=5000):Hace que la app sea accesible desde otros dispositivos de la misma red,(port=5000):Puerto donde la app escucha (puedes abrir http://localhost:5000).     
