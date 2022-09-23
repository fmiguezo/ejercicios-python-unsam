# ejercicio 4.3
#%%
def buscar_u_elemento(lista, e):
    pos = -1  # valor por default sin "e" no está en la lista
    i = 0  # contador
    for z in lista:  # recorro la lista
        if (
            z == e
        ):  # si el elemento de la lista que estoy iterando es igual al elemento que quiero buscar
            pos = i  # la posición en la lista es i
            # no pongo break para que siga iterando y busque todas las posiciones de e, para que sólo muestre la última que aparece
        i += 1
    return pos


buscar_u_elemento([1, 2, 3, 2, 3, 4], 1)  # 0
buscar_u_elemento([1, 2, 3, 2, 3, 4], 2)  # 3
buscar_u_elemento([1, 2, 3, 2, 3, 4], 3)  # 4
buscar_u_elemento([1, 2, 3, 2, 3, 4], 5)  # -1

#%%
def buscar_n_elemento(lista, e):
    i = 0  # contador
    for z in lista:  # recorro la lista
        if (
            z == e
        ):  # si el elemento de la lista que estoy iterando es igual al elemento que quiero buscar
            # no pongo break para que siga iterando y busque todas las posiciones de e, para que sólo muestre la última que aparece
            i += 1
    return i


buscar_n_elemento([1, 2, 3, 2, 3, 4], 1)  # 1
buscar_n_elemento([1, 2, 3, 2, 3, 4], 2)  # 2
buscar_n_elemento([1, 2, 3, 2, 3, 4], 3)  # 2
buscar_n_elemento([1, 2, 3, 2, 3, 4], 5)  # 0

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

    if not (lista):
        print("Lista vacía")
        return None
    m = -float("inf")


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
