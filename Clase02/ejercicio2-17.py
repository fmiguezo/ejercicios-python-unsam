import csv


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
