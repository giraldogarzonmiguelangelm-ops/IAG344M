#CHATBOT SUPERVISADO
#scikit-learn
import os #Hace la conexión entre rutas
import pickle #Aquí creo que es donde se guarda las rutas
from sklearn.feature_extraction.text import CountVectorizer #Convierte texto en vector
from sklearn.naive_bayes import MultinomialNB #Nos permite agarrar el texto y analiza la posible respuesta funcionando como un interprete, es la conexion entre el texto y lo que el conoce para dar la mejor respuesta

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
ANSWERS_PATH = os.path.join(MODEL_DIR, "answers.pkl")

#Función de entrenamiento preguntas y respuestas
def build_and_train_model(train_pairs):   #El chatbot va a entrenar por pares(pregunta,respuesta)
    #train_pairs lista de pares(pregunta, respuestas)
    #Ejemplo [("Hola", "!Hola¡"),("adios", "!Hasta luego¡")]
    #Separamos las preguntas y respuestas en dos listas
    questions = [q for q, _ in train_pairs] #Lista de preguntas
    answers = [a for _, a in train_pairs] #Lista de respuestas
    #Creamos el vectorizado, que traducira el texto a numeros
    vectorizer = CountVectorizer()
    #Entrenamiento 
    x = vectorizer.fit_transform(questions) #Transforma preguntas en numeros
    #Obtenemos una lista de respuestas unicas
    unique_answers = sorted(set(answers))
    #Crea el diccionario con las etiquetas 
    answers_to_label = {a: i for i, a in enumerate(unique_answers)}
    #Creamos una lista 
    y = [answers_to_label[a] for a in answers]
    #Modelo clasificación de texto
    model = MultinomialNB()
    #Entrenar el modelo
    model.fit(x,y)
    
    #Crear carpeta para guardar model si no existe
    os.makedirs(MODEL_DIR, exist_ok = True)
    #Guardar los objetos entrenados
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model,f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)
    with open(ANSWERS_PATH, "wb") as f:
        pickle.dump(unique_answers, f)
        print(" 🆗 Modelo entrenado y guardado correctamente")
    return model,vectorizer,unique_answers

def load_model():
    """
    Carga el modelo, el vectorizado y las respuestas si existe. 
    """
    if(
        os.path.exists(MODEL_PATH)
        and os.path.exists(VECTORIZER_PATH)
        and os.path.exists(ANSWERS_PATH)
    ):
        with open(MODEL_PATH,"rb") as f:
            model = pickle.load(f)
        with open(VECTORIZER_PATH,"rb") as f:
            vectorizer = pickle.load(f)
        with open(ANSWERS_PATH,"rb") as f:
            unique_answers = pickle.load(f)
        print("📂 Modelo cargado desde disco.")
        return model, vectorizer, unique_answers
    else:
        print("⚠️ No hay modelo guardado, será necesario entrenarlo")
        return None, None, None
#Función predict_answer
def predict_answer(model, vectorizer, unique_answers, user_text):
    #Convertimos el texto a numeros
    x = vectorizer.transform([user_text])
    #El modelo predice la etiqueta de la respuesta correcta
    label = model.predict(x)[0]
    return unique_answers[label]
