# Ejercicio 12.7:


def merge_sort(lista, comparaciones=0):
    """Ordena lista mediante el método merge sort.
    Pre: lista debe contener elementos comparables.
    Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, comparaciones = merge_sort(lista[:medio], comparaciones)
        der, comparaciones = merge_sort(lista[medio:], comparaciones)
        merge_res = merge(izq, der)
        lista_nueva = merge_res[0]
        comparaciones += merge_res[1]
    return lista_nueva, comparaciones


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
    Pre: lista1 y lista2 deben estar ordenadas.
    Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comparaciones = 1
    while i < len(lista1) and j < len(lista2):
        comparaciones += 1
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comparaciones


lista = [6, 0, 3, 2, 5, 7, 4, 1]
merge_sort(lista)
