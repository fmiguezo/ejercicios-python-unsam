## Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
import csv
import matplotlib.pyplot as plt
import numpy as np


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
