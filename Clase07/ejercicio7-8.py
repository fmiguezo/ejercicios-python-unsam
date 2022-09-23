# Ejercicio 7.8: Sumas


def sumar_enteros(desde, hasta):
    """Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    """
    suma = 0
    if hasta < desde:
        pass
    else:
        for i in range(desde, hasta + 1):
            suma = suma + i
    return suma


def sumar_enteros2(n):
    return (n * (n + 1)) / 2
