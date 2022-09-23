# documentacion.py
# Ejercicio 7.10: Funciones y documentación
#%%
def valor_absoluto(n):
    """
    Devuelve el valor absoluto de un número real
    Pre: "n" es un número real
    Pos: devuelve el valor absoluto de n
    """
    if n >= 0:
        return n
    else:
        return -n


#%%
def suma_pares(l):
    """
    Suma los valores pares de una lista.
    Pre: l debe ser una lista con números.
    Pos: devuelve la suma de los valores de la lista que sean pares
    """
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0

    return res
    # Inv: res contiene el valor de la suma de los valores pares de la lista


#%%
def veces(a, b):
    """
    Suma una varias veces un número ingresado.
    a : número que va a sumar
    b : veces

    Pre: a debe ser un número. b debe ser mayor o igual que 0.
    Pos: devuelve la suma de a, b veces
    """
    res = 0
    nb = b
    while nb != 0:
        # print(nb * a + res)
        res += a
        nb -= 1
    return res
    # Inv: res es igual a: a * (b - nb)


#%%
def collatz(n):
    """
    Prueba la conjetura de Collatz. Dado un número entero positivo, calcula la
    se cancula la cantidad de operaciones que hay que realizar para llegar a 1.
    Se aplica la siguiente operación: si n es par se divide entre 2; si n es
    impar se multiplica por 3 y se suma 1.
    Pre: n debe ser un número entero positivo
    Pos: devuelve la cantidad de operaciones necesarias para llegar a 1.
    """
    res = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res += 1

    return res
    # Inv: res contiene la cantidad de operaciones requeridas n llegue a 1
