# ejercicio 4.2

import csv

from pprint import pprint

## original
# def leer_camion(nombre_archivo):
#     camion = []
#     registro = {}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1]) #reemplaza el valor del registro appendeado en camión
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

## debuggeado
def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = (
                {}
            )  # si muevo registro dentro del for, se limpia la variable y agrega los nuevos valores en lugar de reemplazarlos
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion


camion = leer_camion("../Data/camion.csv")
pprint(camion)
