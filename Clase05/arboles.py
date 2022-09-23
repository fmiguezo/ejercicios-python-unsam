# Ejercicios 5.25 / 5.26 / 5.27

#%% 5.25
## Ejercicio 5.25: Histograma de altos de Jacarandás
#%%
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import sys


def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = [headers.index(ncolumna) for ncolumna in headers]
        row = next(rows)
        arboleda = [
            {ncolumna: row[index] for ncolumna, index in zip(headers, indices)}
            for row in rows
        ]
        return arboleda


def grafico_altura_jacaranda(archivo_arboles):
    arboleda = leer_arboles(archivo_arboles)
    altos = [
        float(arbol["altura_tot"])
        for arbol in arboleda
        if arbol["nombre_com"] == "Jacarandá"
    ]
    plt.figure()
    plt.hist(altos, bins=70)
    plt.xlabel("Alturas de los árboles")
    plt.ylabel("Cantidad de árboles")
    plt.title("Alturas de los Jacarandás del arbolado porteño")
    return plt


def main():
    archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"
    grafico_altura_jacaranda(archivo_arboles)


# %%

##5.26
#%%
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = [headers.index(ncolumna) for ncolumna in headers]
        row = next(rows)
        arboleda = [
            {ncolumna: row[index] for ncolumna, index in zip(headers, indices)}
            for row in rows
        ]
        return arboleda


def scatter_hd(lista_de_pares):
    lista = np.array(lista_de_pares)
    h = lista[0:, 0]
    d = lista[0:, 1]
    colors = np.random.rand(len(lista_de_pares))
    area = (20 * np.random.rand(len(lista_de_pares))) ** 2  # 0 to 15 point radii
    plt.scatter(d, h)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.scatter(d, h, s=area, c=colors, alpha=0.5)
    plt.show()
    return


def main():
    archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"
    parque = ""
    arboleda = leer_arboles(archivo_arboles)
    lista_de_pares = [
        (float(arbol["altura_tot"]), float(arbol["diametro"]))
        for arbol in arboleda
        if arbol["nombre_com"] == "Jacarandá"
    ]
    scatter_hd(lista_de_pares)


## 5.27

#%%
def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = [headers.index(ncolumna) for ncolumna in headers]
        row = next(rows)
        arboleda = [
            {ncolumna: row[index] for ncolumna, index in zip(headers, indices)}
            for row in rows
        ]
        return arboleda


def medidas_de_especies(especies, arboleda):
    dic = {
        x: [
            (float(arbol["altura_tot"]), float(arbol["diametro"]))
            for arbol in arboleda
            if arbol["nombre_com"] == x
        ]
        for x in especies
    }
    # for x in especies:
    #     dic[x] = [
    #     (float(arbol["altura_tot"]), float(arbol["diametro"]))
    #     for arbol in arboleda
    #     if arbol["nombre_com"] == x]
    return dic


def scatter_hd(medidas):
    for especie in medidas:
        lista = np.array(medidas[especie])
        colors = np.random.rand(len(medidas[especie]))
        area = (20 * np.random.rand(len(medidas[especie]))) ** 2  # 0 to 15 point radii
        h = lista[0:, 0]
        d = lista[0:, 1]
        plt.scatter(d, h)
        plt.xlabel("diametro (cm)")
        plt.ylabel("alto (m)")
        plt.xlim(0, 300)
        plt.ylim(0, 50)
        plt.title(f"Relación diámetro-alto para {especie}".format(especie))
        plt.scatter(d, h, s=area, c=colors, alpha=0.5)
        plt.show()
    return


#%% Función principal
def f_principal(argv):
    archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"
    arboleda = leer_arboles(archivo_arboles)
    especies = ["Eucalipto", "Palo borracho rosado", "Jacarandá"]
    medidas = medidas_de_especies(especies, arboleda)
    scatter_hd(medidas)


if __name__ == "__main__":
    f_principal(sys.argv)
