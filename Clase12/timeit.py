import time
import timeit as tt
import random
import numpy as np
import matplotlib.pyplot as plt


def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica el número de veces que repite el ordenamiento para cada lista.
    """
    tiempos_seleccion = []

    global lista

    for lista in listas:

        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit(
            "ord_seleccion(lista.copy())", number=num, globals=globals()
        )

        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)

    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)

    return tiempos_seleccion


# generar lista
def generar_lista(N):
    """Genera una lista aleatoria de largo N con números enteros del 1 al 1000
    (puede haber repeticiones)."""
    lista = [0] * N
    for i in range(N):
        lista[i] = random.randint(0, 1000)
    return lista


# -------------------------------- #
# ordenamiento por selección


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada."""
    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    comparaciones = 0
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        comparaciones += n - 0
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # reducir el segmento en 1
        n = n - 1
    return comparaciones


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
    lista de elementos comparables.
    La lista no debe ser vacía.
    a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))

tiempos_seleccion = experimento_timeit_seleccion(listas, 100)
plt.plot(tiempos_seleccion)
