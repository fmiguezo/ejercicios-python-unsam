# Ejercicio 8.2: Cuánto falta

from datetime import date


def cuantofalta():
    hoy = date.today()
    primavera2022 = date(2022, 9, 21)
    cuanto = primavera2022 - hoy
    print(cuanto)


cuantofalta()
