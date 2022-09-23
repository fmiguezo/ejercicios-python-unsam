# burbujeo.py
# Ejercicio 12.2: burbujeo


def ord_burbujeo(lista):
    n = len(lista)
    for pasada in range(n - 1, 0, -1):
        for i in range(pasada):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista
