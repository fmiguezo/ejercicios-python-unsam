## Ejercicio 5.8: Guardar temperaturas
import random
import numpy as np

#%%
def medir_temp(n):
    temperaturas = [round(random.normalvariate(37.5, 0.2), 2) for _ in range(n)]
    np.save("../Data/temperaturas.npy", temperaturas)
    return temperaturas


#%%
def resumen_temp(n):
    lista = medir_temp(n)
    maximo = max(lista)
    minimo = min(lista)
    promedio = round(sum(lista) / n, 2)
    lista.sort()
    long = len(lista)
    mitad = int(long / 2)
    if long % 2 == 0:
        mediana = (lista[mitad - 1] + lista[mitad]) / 2
    else:
        mediana = lista[mitad]
    mediana = round(mediana, 2)
    return maximo, minimo, promedio, mediana


n = 999
