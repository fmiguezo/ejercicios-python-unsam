import csv
import sys


def costo_camion(nombre_archivo):
    f = open(nombre_archivo, "rt")
    rows = csv.reader(f)
    headers = next(rows)
    costo_total = 0
    try:
        for line in f:
            line = line.strip()
            row = line.split(",")
            row.pop(0)
            cantidad = int("".join(row[0]))
            precio = float("".join(row[1]))
            costo_cajon = cantidad * precio
            costo_total = costo_total + costo_cajon
        f.close()
        return costo_total
    except:
        print("Falta información")


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = "../Data/camion.csv"

costo = costo_camion(nombre_archivo)
print("Costo total:", costo)
