# busqueda_en_listas.py
# Ejercicio 6.13: Búsqueda lineal sobre listas ordenadas.

#%%
def busqueda_lineal_lordenada(lista, e):
    """Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    """
    pos = -1  # comenzamos suponiendo que e no está
    lista.sort()
    for i, z in enumerate(lista):  # recorremos la lista
        if z > e:  # primer elemento mayor a e
            pos = i  # guardamos su posición
            break  # y salimos del ciclo
    return pos
