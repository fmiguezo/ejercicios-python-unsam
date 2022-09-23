"""
Ejercicio 5.3: Cocumpleaños
Haciendo miles de experimentos numéricos, estimá la probabilidad de que en un grupo de 30 personas elegidas al azar, dos cumplan años el mismo día. Escribí un programita que permita calcular esa probabilidad asumiendo que el año tiene 365 días.
Modificando un poco tu programa anterior, ¿podés calcular cuántas personas tiene que haber en un grupo para que sea más probable que dos cumplan años el mismo día que que todas cumplan en días diferentes?
# p(c) + p(d) = 1
# p(c) = 1 - p(d)
# x = 30
# (365!/(363-x)!)/365**x
# 0.2936 
# 29.36%
# p(c) = 1 - p(d) = 1 - 0.2936 = 0.7063 ~ 70.6%
"""
## con módulo math y factorial
from math import factorial

n = 30
pd = (factorial(365) / factorial(365 - n)) / 365 ** n
pc = 1 - pd

## sin módulo math
def cocumpleanios(n):
    pd = 1
    for i in range(n):
        pd = pd * ((365 - i) / 365)
    pc = 1 - pd
    return pc
