#Librerias
import re   #Activa la libreria
"""
Expresiones regulares en Python
Problemas Reales

"""
#Código 
print("Libreria cargada correctamente")
#Ejemplo 1
texto = "Mi número es 1234"
resultado = re.search(r"\d+", texto) #Busca los numeros que se encuentren en la variable texto
print(resultado.group())   #Muestra el resultado de la busqueda
print(f"{texto} Resultado: {resultado.group()}") #Con la f y {} se reemplaza la concatenación regular para imprimir lo lo que esta dentro de los {}
texto = "Mi numero es 12345-985"
resultado = re.search(r"\d+",texto)
print(f"{texto} Resultado: {resultado.group()}")
resultado = re.findall(r"\d+",texto)   #Findall busca y pone todos los elementos que encuentre en una lista
print(f"{texto} Resultado: {resultado}")

documento = "cc.75.055.60"

def clean_id(documento):       #Esto es una funcion que limpia el id y solo deja los numeros
    return re.sub(r"\D","",documento)   #sub reemplaza la expresión regular por lo que se le indique, en este caso ""(nada)
print(clean_id(documento))


