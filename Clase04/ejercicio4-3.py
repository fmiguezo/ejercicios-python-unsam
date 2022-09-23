# ejercicio 4.3


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
