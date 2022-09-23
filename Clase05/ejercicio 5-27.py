## Ejercicio 5.27: Scatterplot para diferentes especies
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


def main():
    archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"
    arboleda = leer_arboles(archivo_arboles)
    especies = ["Eucalipto", "Palo borracho rosado", "Jacarandá"]
    medidas = medidas_de_especies(especies, arboleda)
    scatter_hd(medidas)
