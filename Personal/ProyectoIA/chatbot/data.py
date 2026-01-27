# chatbot/data.py

# Lista de motos
motos = [
    {"modelo": "Scrambler Icon", "tipo": "Urbana", "cilindraje": 803, "experiencia": "Principiante", "uso": "Ciudad"},
    {"modelo": "Monster", "tipo": "Naked", "cilindraje": 937, "experiencia": "Intermedio", "uso": "Ciudad"},
    {"modelo": "Multistrada V2", "tipo": "Aventura", "cilindraje": 937, "experiencia": "Intermedio", "uso": "Viajes"},
    {"modelo": "Multistrada V4", "tipo": "Aventura", "cilindraje": 1158, "experiencia": "Experto", "uso": "Viajes"},
    {"modelo": "Panigale V2", "tipo": "Deportiva", "cilindraje": 955, "experiencia": "Experto", "uso": "Velocidad"},
    {"modelo": "Panigale V4", "tipo": "Deportiva", "cilindraje": 1103, "experiencia": "Experto", "uso": "Velocidad"},
    {"modelo": "DesertX", "tipo": "Doble propósito", "cilindraje": 937, "experiencia": "Intermedio", "uso": "Mixto"},
]

# Generar training_data para chatbot
training_data = []

for moto in motos:
    # Preguntas típicas que un usuario podría hacer
    training_data.append((
        f"Quiero una moto para {moto['uso']} y soy {moto['experiencia']}", 
        f"Te recomiendo la {moto['modelo']}"
    ))
    training_data.append((
        f"¿Qué moto {moto['tipo']} me recomiendas?", 
        f"Te recomiendo la {moto['modelo']}"
    ))
    training_data.append((
        f"Busco una moto con cilindraje {moto['cilindraje']} cc", 
        f"La {moto['modelo']} tiene {moto['cilindraje']} cc"
    ))
