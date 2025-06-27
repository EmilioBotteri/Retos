

"""
🎉 Pregunta de la Semana @everyone  🚀
🌸🐣 Especial Pascua y Sant Jordi 📚🐉

💡 ¡Caza de Huevos o Regalo de Libros!

Esta semana celebramos dos fechas muy especiales: la Pascua y Sant Jordi. Así que tu reto será
 elegir un camino… 🐰 o 🐉

🔹 Pregunta (elige 1 de las 2 misiones):

🟢 Opción 1: La Caza de Huevos (Pascua)
Imagina un jardín lleno de huevos de Pascua con diferentes premios. Están guardados en una lista,
y cada huevo tiene un valor sorpresa.

👉 Crea una función que simule la búsqueda de huevos, y:

Recorra la lista con un bucle
Sume los puntos recogidos
Diga cuántos huevos "especiales" (por ejemplo, los que valen más de 10) encontró

🔴 Opción 2: La Rosa y el Libro (Sant Jordi)
Cada persona en una lista recibe un libro y una rosa, pero algunos están repetidos.

👉 Crea una función que:

Reciba una lista de regalos entregados
Cuente cuántas veces se repite cada libro y cada rosa
Devuelva un resumen indicando los regalos más populares

✍️ Pistas para ambas misiones:

Usa funciones para organizar tu lógica

Usa bucles para recorrer las listas

Puedes usar condicionales y estructuras como count() o diccionarios para contar

Hazlo divertido: ¡invéntate nombres de huevos, rosas o libros!

🎯 Puntos Extra:
✅ Si haces ambas misiones
✅ Si usas funciones reutilizables
✅ Si tu código muestra resultados con estilo y claridad

🔥 ¡Elige tu aventura y celebra programando! ¿Eres más de chocolate o de historias épicas? 🐣📖
"""
import random 

lista_huevos = [3, 12, 25, 8, 5, 47, 2, 7, 0, 6, 4, 4, 11, 8, 10, 23, 5, 6, 4, 3, 2, 2, 1, 22]

def cantidad_huevos(tiempo:int):
    if tiempo <= 1:
        cant_huevos = 5
    elif tiempo <= 3:
        cant_huevos = 8
    else:
        cant_huevos = 12
        
    return cant_huevos


def recolectar(tiempo):
    contador = 0
    puntos = 0
    especiales = 0

    cant_huevos = cantidad_huevos(tiempo)
    for i in random.sample(lista_huevos, cant_huevos):
        if i >= 10:
            especiales += 1
        puntos += i
    
    resultado(cant_huevos, puntos, especiales)

def resultado(cant_huevos, puntos, especiales):

    print(f"Has recolectado {cant_huevos} huevos. En total sumaste {puntos} puntos y obtuviste {especiales} huevos especiales!!!")


recolectar(int(input("Ingrese la cantidad de horas que va a recolectar huevos: ")))


# EJERCICIO SANT JORDI

lista_regalos = ["Rosa negra", "El principito", "Palo de escoba", "Rosa", "La psicologia del dinero", "Ramo de flores", "Rosa", "El principito", "Rosa", "Rosa negra"]

def contar_regalos(lista:list):
    dicc = {}
    for i in lista:
        if i in dicc:
            dicc[i] += 1
        else:
            dicc[i] = 1
    mostrar(dicc)

def mostrar(diccionario:dict):
    for k, v in diccionario.items():
        print(f"El regalo -{k}- se ha repetido {v} veces")


contar_regalos(lista_regalos)


