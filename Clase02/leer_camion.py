import csv
from pprint import pprint


def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            lote = {"nombre": row[0], "cajones": int(row[1]), "precio": float(row[2])}
            camion.append(lote)
    return camion


camion = leer_camion("../Data/camion.csv")
