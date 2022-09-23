## Ejercicio 5.13: Cantidad de compras

import random
import numpy as np

#%%
def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album


#%%
def album_incompleto(A):
    ordenado = np.sort(A)
    if ordenado[0] == 0:
        return True
    else:
        return False


#%%
def comprar_figu(figus_total):
    figurita = random.randint(1, figus_total)
    return figurita


#%%
def cuantas_figus(figus_total):
    figuritas_compradas = 0
    A = crear_album(figus_total)
    while album_incompleto(A) == True:
        A[comprar_figu(figus_total) - 1] += 1
        figuritas_compradas += 1
    return figuritas_compradas


figus_total = 670
