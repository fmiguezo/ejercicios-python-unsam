# Ejercicio 5.17:
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


#%%
# n_repeticiones = 1000
# figus_total = 6
# lista = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
# promedio = np.mean(lista)


def experimento_figus(n_repeticiones, figus_total):
    lista = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    promedio = np.mean(lista)
    return promedio


# n_repeticiones = 100
# figus_total = 670

# figus_total = 670
# paquete = np.array([random.randint(1,figus_total) for _ in range(5)])

# Ejercicio 5.17:
def comprar_paquete(figus_total, figus_paquete):
    return [random.randint(1, figus_total) for _ in range(figus_paquete)]


figus_total = 670
figus_paquete = 5
