# solucion_de_errores.py
# Ejercicios de errores en el código
#%%
# Ejercicio 3.1. Función tiene_a()
# Comentario: En el caso #1 y #3 da False cuando debería ser True.
# El error es que para las palabras que no empiezan con "a", el while retorna falso y termina la ejecución,
# no sigue buscando en las demás letras del string.
#    Lo corregí sacando el else del while, y poniendo un "return False" fuera del while, para que retorne falso
# si la oración no tiene a. Agregué un .lower() a la condición del while para que convierta las mayúsculas a
# minúsculas, para que tome las "A" como True
#    A continuación va el código corregido


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i].lower() == "a":
            return True
        i += 1
    return False


tiene_a("UNSAM 2020")  # True
tiene_a("abracadabra")  # True
tiene_a("La novela 1984 de George Orwell")  # True

#%%
# Ejercicio 3.2. Función tiene_a(), nuevamente
# Errores: faltan ":" luego de la función y el while, el if dentro del while debería tener un == y no un =, y el return debería ser False y no Falso
# Comentario: además de esos errores, no evalúa las mayúsculas. Lo solucioné con un .lower() en la condición del while
#    A continuación va el código corregido
## corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i].lower() == "a":  # acá agregué el .lower()
            return True
        i += 1
    return False


tiene_a("UNSAM 2020")
tiene_a("La novela 1984 de George Orwell")

#%%
# Ejercicio 3.3. Función tiene_uno()
# Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
# tiene_uno(1984) #da error porque el tipo 'int' no tiene len, hay que convertir la expresion a un string
# Lo solucioné agregando "expresion = str(expresion)" a la primera línea de la función
#    A continuación va el código corregido
## corregido
def tiene_uno(expresion):
    expresion = str(expresion)  # esta es la línea que agregué
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == "1":
            tiene = True
        i += 1
    return tiene


tiene_uno("UNSAM 2020")
tiene_uno("La novela 1984 de George Orwell")
tiene_uno(1984)


#%%
# Ejercicio 3.4: Alcances
# Comentario: a la función le falta el return por eso no devuelve ningún valor, le agregué el "return c" en la
# última línea para que devuelva el valor de c
#    A continuación va el código corregido
## corregido
def suma(a, b):
    c = a + b
    return c  # ésta es la línea que agregué


a = 2
b = 3
c = suma(a, b)
print(f"La suma da {a} + {b} = {c}")


#%%
# Ejercicio 3.5: Pisando memoria
#%%
# Ejercicio 3.5: Pisando memoria
# Comentario: con un print probe que el for itera sobre cada línea, pero lo que agrega a camión es siempre la
# última línea del archivo al diccionario porque el registro está definido fuera del for
# Solución: "registro" es un diccionario, por lo cuál para que agregué cada una de las líneas a "camion" en ese
# formato, hay que reemplazar el valor de "registro" como planteado en la solución

#    A continuación va el código corregido

import csv
from pprint import pprint


def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {
                encabezado[0]: fila[0],
                encabezado[1]: int(fila[1]),
                encabezado[2]: float(fila[2]),
            }
            camion.append(registro)
    return camion


camion = leer_camion("../Data/camion.csv")
pprint(camion)
