import csv
from pprint import pprint


def cajones_camion(nombre_archivo):
    cajones = {}

    with open(nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            if row[0] not in cajones:
                cajones[row[0]] = int(row[1])
            else:
                cajones[row[0]] = int(row[1]) + cajones[row[0]]
    return cajones


cajones = cajones_camion("../Data/camion.csv")


def leer_precios(nombre_archivo):
    precios = {}  # Empezamos con un diccionario vacío

    with open(nombre_archivo, "rt") as f:
        for line in f:
            try:
                row = line.split(",")
                precios[row[0]] = float(row[1])
            except IndexError:
                pass
    return precios


precios = leer_precios("../Data/precios.csv")


total_venta = 0.0
for s in cajones:
    total_venta += cajones[s] * precios[s]
