## figuritas.py
import random
import numpy as np
import matplotlib.pyplot as plt

#%%
def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album


#%%
def album_incompleto(A):
    if 0 in A:
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
def experimento_figus(n_repeticiones, figus_total):
    lista = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    promedio = np.mean(lista)
    return promedio


#%%
def comprar_paquete(figus_total, figus_paquete):
    return [random.randint(1, figus_total) for _ in range(figus_paquete)]


#%%
def cuantos_paquetes(figus_total, figus_paquete):
    paquetes = 0
    A = crear_album(figus_total)
    while album_incompleto(A) == True:
        for _ in comprar_paquete(figus_total, figus_paquete):
            A[comprar_figu(figus_total) - 1] += 1
        paquetes += 1
    return paquetes


## Graficar el llenado del álbum
#%%
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop() - 1] = 1
        figus_pegadas = (album > 0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas


## Ejercicio 5.19:
#%%
def main():
    n_repeticiones = 100
    figus_total = 670
    figus_paquete = 5
    lista = [
        cuantos_paquetes(figus_total, figus_paquete) for _ in range(n_repeticiones)
    ]
    promedio = np.mean(lista)

    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()
