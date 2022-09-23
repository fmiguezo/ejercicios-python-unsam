# comparaciones_ordenamiento.py
# Ejercicio 12.4: experimento con 3 métodos
# Ejercicio 12.5: comparar métodos gráficamente
# Ejercicio 12.7:


import random
import matplotlib.pyplot as plt

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


# -------------------------------- #
# ordenamiento por inserción


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada."""
    contador = 0
    reubi = ()
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubi = reubicar(lista, i + 1)
            contador += reubi[1]
    return contador


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
    dentro del segmento [0:p-1].
    Pre: p tiene que ser una posicion válida de lista."""
    v = lista[p]
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    contador = 0
    while j > 0 and v < lista[j - 1]:
        contador += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v
    return v, contador


# -------------------------------- #
# ordenamiento por burbujeo


def ord_burbujeo(lista):
    """El algoritmo compara dos elementos contiguos de la lista y, si el orden es adecuado, los deja como están,
    si no, los intercambia."""
    n = len(lista)
    cambios = None
    comparaciones = 0
    while cambios != False:
        cambios = False
        comparaciones += n - 1
        n -= 1
        for i in range(n - 1):
            if lista[i - 1] > lista[i]:
                lista[i - 1], lista[i] = lista[i], lista[i - 1]
                cambios = True
    return comparaciones


# experimento
def experimento(N, k):
    """Repite k veces lo siguiente: generar una lista de largo N, ordenar la lista con los tres métodos y
    guardar la cantidad de operaciones. Al final, la función devuelve el promedio de comparaciones
    realizadas con cada método."""
    sum_sel = 0
    sum_ins = 0
    sum_bur = 0
    for i in range(k):
        lista = generar_lista(N)
        sel = ord_seleccion(lista.copy())
        ins = ord_insercion(lista.copy())
        bur = ord_burbujeo(lista.copy())
        sum_sel += sel
        sum_ins += ins
        sum_bur += bur
    return (sum_sel / k, sum_ins / k, sum_bur / k)


# generar Nmax listas
def generar_listas(Nmax):
    listas = [generar_lista(e) for e, s in enumerate(range((Nmax)), start=1)]
    return listas


# -----------------------------------#
# merge sort #


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
    contador = 1
    while i < len(lista1) and j < len(lista2):
        contador += 1
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, contador


# experimento vectores
def experimento_vectores(Nmax):
    """Para N entre 1 y Nmax genera una lista de largo N con números enteros del 1 al 1000 en orden
    aleatorio, calcule la cantidad de comparaciones realizadas por cada método de ordenamiento y
    guarde estos resultados en tres vectores de largo Nmax: comparaciones_seleccion,
    comparaciones_insercion y comparaciones_burbujeo."""
    listas = generar_listas(Nmax)
    comparaciones_seleccion = []
    comparaciones_insercion = []
    comparaciones_burbujeo = []
    comparaciones_mergesort = []
    for lista in listas:
        comparaciones_seleccion.append(ord_seleccion(lista.copy()))
        comparaciones_insercion.append(ord_insercion(lista.copy()))
        comparaciones_burbujeo.append(ord_burbujeo(lista.copy()))
        comparaciones_mergesort.append(merge_sort(lista.copy())[1])

    # plot
    plt.xlim([0, 300])
    plt.ylim([0, 30000])
    # plt.xlabel("x")
    # plt.ylabel("y")
    plt.plot(comparaciones_seleccion, label="Selección")
    plt.plot(comparaciones_insercion, label="Inserción")
    plt.plot(comparaciones_burbujeo, "r--", label="Burbujeo")
    plt.plot(comparaciones_mergesort, label="Merge sort")
    plt.title("Cantidad de comparaciones")
    plt.legend()
    plt.show()
