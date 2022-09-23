# Ejercicio 4.16: Lista de altos de Jacarandá
#%%
import csv


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


archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"
parque = ""
arboleda = leer_arboles(archivo_arboles)

H = [
    float(arbol["altura_tot"])
    for arbol in arboleda
    if arbol["nombre_com"] == "Jacarandá"
]
