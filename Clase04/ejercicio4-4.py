# ejercicio 4.4
#%%
def maximo(lista):
    """Devuelve el máximo de una lista,
    la lista debe ser no vacía y de números positivos.
    """
    # if not(lista):
    #     print("Lista vacía")
    #     return None
    # m = -float("inf") // trae -infinito y sirve para que no de error si la lista está vacía
    # m guarda el máximo de los elementos a medida que recorro la lista.
    m = lista[0]  # Lo inicializo en el primer valor de la lista
    for e in lista:  # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m


maximo([1, 2, 7, 2, 3, 4])  # 7
maximo([1, 2, 3, 4])  # 4
maximo([-5, 4])  # 4
maximo([-5, -4])  # 0

#%%
def minimo(lista):
    m = lista[0]  # Lo inicializo en el primer valor de la lista
    for e in lista:  # Recorro la lista y voy guardando el menor
        if e < m:
            m = e
    return m


minimo([1, 2, 7, 2, 3, 4])  # 1
minimo([1, 2, 3, 4])  # 1
minimo([-5, 4])  # -5
minimo([-5, -4])  # -4
minimo([-5, -10])  # -10
