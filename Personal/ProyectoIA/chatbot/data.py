# chatbot/data.py

# Lista de motos
motos = [
    {"modelo": "Scrambler Icon", "tipo": "Urbana", "cilindraje": 803, "experiencia": "Principiante", "uso": "Ciudad", "precio_min_usd": 13000, "precio_max_usd": 16000 },     
    {"modelo": "Scrambler Icon Dark", "tipo": "Scrambler", "cilindraje": 803, "experiencia": "Intermedio", "uso": "Urbana / Lifestyle", "precio_min_usd": 10000, "precio_max_usd": 15000},
    {"modelo": "Scrambler Nightshift", "tipo": "Scrambler", "cilindraje": 803, "experiencia": "Intermedio", "uso": "Urbana / Lifestyle", "precio_min_usd": 10000, "precio_max_usd": 15000},
    {"modelo": "Scrambler Full Throttle", "tipo": "Scrambler", "cilindraje": 803, "experiencia": "Intermedio", "uso": "Urbana / Sport", "precio_min_usd": 12000, "precio_max_usd": 16000},
    {"modelo": "Monster", "tipo": "Naked", "cilindraje": 937, "experiencia": "Intermedio", "uso": "Ciudad", "precio_min_usd": 15000, "precio_max_usd": 18000},     
    {"modelo": "Nueva Monster", "tipo": "Naked", "cilindraje": 937, "experiencia": "Intermedio", "uso": "Urbana / Sport", "precio_min_usd": 14000, "precio_max_usd": 18000},
    {"modelo": "Monster V2", "tipo": "Naked", "cilindraje": 890, "experiencia": "Intermedio", "uso": "Urbana / Sport", "precio_min_usd": 15000, "precio_max_usd": 19000},
    {"modelo": "Multistrada V2", "tipo": "Aventura", "cilindraje": 937, "experiencia": "Intermedio", "uso": "Viajes", "precio_min_usd": 17000, "precio_max_usd": 24000 },
    {"modelo": "Multistrada V4", "tipo": "Aventura", "cilindraje": 1158, "experiencia": "Experto", "uso": "Viajes", "precio_min_usd": 24000, "precio_max_usd": 30000},
    {"modelo": "Multistrada V4 S", "tipo": "Adventure / Touring", "uso": "Viajes", "cilindraje": 1158, "experiencia": "Experto", "precio_min_usd": 25000, "precio_max_usd": 40000},
    {"modelo": "Multistrada V4 Pikes Peak", "tipo": "Adventure / Touring", "uso": "Viajes / Off-road", "cilindraje": 1158, "experiencia": "Experto", "precio_min_usd": 28000, "precio_max_usd": 42000},
    {"modelo": "Panigale V2", "tipo": "Deportiva", "uso": "Velocidad / Pista", "cilindraje": 955, "experiencia": "Experto", "precio_min_usd": 18000, "precio_max_usd": 25000},
    {"modelo": "Panigale V4", "tipo": "Deportiva", "cilindraje": 1103, "experiencia": "Experto", "uso": "Velocidad", "precio_min_usd": 28000, "precio_max_usd": 35000},
    {"modelo": "Panigale V2 S", "tipo": "Deportiva", "uso": "Velocidad / Pista", "cilindraje": 955, "experiencia": "Experto", "precio_min_usd": 20000, "precio_max_usd": 28000},
    {"modelo": "Panigale V4 S", "tipo": "Deportiva", "uso": "Velocidad / Pista", "cilindraje": 1103, "experiencia": "Experto", "precio_min_usd": 27000, "precio_max_usd": 45000},       
    {"modelo": "Hypermotard 698 Mono", "tipo": "Motard", "cilindraje": 659, "experiencia": "Intermedio", "uso": "Ciudad / Diversión", "precio_min_usd": 13000, "precio_max_usd": 20000},
    {"modelo": "Nueva Hypermotard V2", "tipo": "Motard", "uso": "Ciudad / Diversión", "cilindraje": 955, "experiencia": "Experto", "precio_min_usd": 18000, "precio_max_usd": 26000 },
    {"modelo": "Nueva Hypermotard V2 SP", "tipo": "Motard", "uso": "Ciudad / Diversión", "cilindraje": 955, "experiencia": "Experto", "precio_min_usd": 17000, "precio_max_usd": 20000 },  
    {"modelo": "Streetfighter V2", "tipo": "Naked Deportiva", "uso": "Sport", "cilindraje": 955, "experiencia": "Experto", "precio_min_usd": 15000, "precio_max_usd": 23000},
    {"modelo": "Streetfighter V4", "tipo": "Naked Deportiva", "uso": "Sport", "cilindraje": 1103, "experiencia": "Experto", "precio_min_usd": 23000, "precio_max_usd": 34500},
    {"modelo": "Streetfighter V4 S", "tipo": "Naked Deportiva", "uso": "Sport", "cilindraje": 1103, "experiencia": "Experto", "precio_min_usd": 29000, "precio_max_usd": 38000},
    {"modelo": "DesertX", "tipo": "Aventura", "uso": "Mixto / Touring", "cilindraje": 937, "experiencia": "Intermedio", "precio_min_usd": 18000, "precio_max_usd": 22000 },     
    {"modelo": "Diavel V4", "tipo": "Cruiser", "uso": "Touring", "cilindraje": 1262, "experiencia": "Experto", "precio_min_usd": 27000, "precio_max_usd": 35000},
    {"modelo": "XDiavel V4", "tipo": "Cruiser", "uso": "Touring / Sport", "cilindraje": 1262, "experiencia": "Experto", "precio_min_usd": 27000, "precio_max_usd": 35000},
    {"modelo": "Desmo450 MX", "tipo": "Off-road / Motocross", "uso": "Competencia / Pista", "cilindraje": 449, "experiencia": "Avanzado", "precio_min_usd": 11000, "precio_max_usd": 15000},
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
