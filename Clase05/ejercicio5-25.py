## Ejercicio 5.25: Histograma de altos de Jacarandás
#%%
import csv
import os
import matplotlib.pyplot as plt


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
