# Ejercicio 11.1


def factorial(n):
    if n == 1:
        r = 1
        return r

    f = factorial(n - 1)
    r = n * f
    return r


def factorial(n):
    """Precondición: n entero positivo
    Devuelve: n!"""
    fact = 1
    for num in range(n, 1, -1):
        fact *= num
    return fact


def potencia(b, n):
    """Precondición: n >= 0
    Devuelve: b^n."""

    if n <= 0:
        # caso base
        return 1

    if n % 2 == 0:
        # caso n par
        p = potencia(b, n // 2)
        return p * p
    else:
        # caso n impar
        p = potencia(b, (n - 1) // 2)
        return p * p * b


def potencia(b, n):
    """Precondición: n >= 0
    Devuelve: b^n."""

    pila = []
    while n > 0:
        if n % 2 == 0:
            pila.append(True)
            n //= 2
        else:
            pila.append(False)
            n = (n - 1) // 2

    p = 1
    while pila:
        es_par = pila.pop()
        if es_par:
            p *= p
        else:
            p *= p * b

    return p


def fib(n):
    """Precondición: n >= 0.
    Devuelve: el número de Fibonacci número n."""
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib(n - 1) + fib(n - 2)
    return res


def fib(n):
    """Precondición: n >= 0.
    Devuelve: el número de Fibonacci número n."""
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n + 1):
        fibn = ant1 + ant2
        ant2 = ant1
        ant1 = fibn
    return fibn
