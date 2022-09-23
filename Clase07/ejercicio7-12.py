# Ejercicio 7.12: Caminatas al azar

import numpy as np
import matplotlib.pyplot as plt
import sys

#%%
def randomwalk(largo):
    """Genera una caminata al azar de N pasos de largo"""
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


#%%
def crear_lista(n, N):
    """Genera una lista de caminatas"""
    lista = []
    for _ in range(n):
        lista.append(randomwalk(N))
    return lista


#%%
def buscar_mayor(lista):
    """Busca la caminata con mayor distancia"""
    inicio = 0
    for caminata in lista:
        max_caminata = abs(max(caminata, key=abs))
        if max_caminata > inicio:
            caminata_mayor = caminata
            inicio = max_caminata
    return caminata_mayor


#%%
def buscar_menor(lista):
    """Busca la caminata con menor distancia"""
    inicio = float("inf")
    for caminata in lista:
        max_caminata = abs(max(caminata, key=abs))
        if max_caminata < inicio:
            caminata_menor = caminata
            inicio = max_caminata
    return caminata_menor


#%%
def cm2inch(value):
    return value / 2.54


#%%
def imprimir_graficos(lista):
    """Imprime los gráficos"""
    fig = plt.figure(figsize=(cm2inch(20), cm2inch(15)))
    # subplot 1
    plt.subplot(2, 1, 1)
    plt.title("12 Caminatas al azar")
    for i in range(len(lista)):
        plt.plot(lista[i])
        plt.ylim(-700, 700)
        plt.yticks([-500, 0, +500]), plt.xticks([])
    # subplot 2
    plt.subplot(2, 2, 3)
    plt.title("La caminata que más se aleja")
    plt.plot(buscar_mayor(lista))
    plt.ylim(-700, 700)
    plt.yticks([-500, 0, +500]), plt.xticks([])
    # subplot 3
    plt.subplot(2, 2, 4)
    plt.title("La caminata que menos se aleja")
    plt.plot(buscar_menor(lista))
    plt.ylim(-700, 700)
    plt.yticks([]), plt.xticks([])

    plt.show()


#%% Función principal
def f_principal(argv):
    N = 100000
    n = 12
    lista = crear_lista(n, N)
    imprimir_graficos(lista)


if __name__ == "__main__":
    f_principal(sys.argv)
