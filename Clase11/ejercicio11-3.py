# Ejercicio 11.3: Dígitos


def cant_digitos(n):
    if n == 0:
        return 0
    return 1 + cant_digitos(n // 10)
