# Ejercicio 11.4: Potencias


def es_potencia(n, b):
    n = n / b
    if n == b:
        return True
    elif n == 1:
        return True
    elif n > b:
        return es_potencia(n, b)
    else:
        return False
