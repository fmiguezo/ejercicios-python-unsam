#%%
# Ejercicio 3.5: Pisando memoria
# Comentario: con un print probe que el for itera sobre cada línea, pero lo que agrega a camión es siempre la
# última línea del archivo al diccionario porque el registro está definido fuera del for
# Solución: "registro" es un diccionario, por lo cuál para que agregué cada una de las líneas a "camion" en ese
# formato, hay que reemplazar el valor de "registro" como planteado en la solución

#    A continuación va el código corregido
## original
# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

# camion = leer_camion('../Data/camion.csv')
# pprint(camion)

import csv
from pprint import pprint


def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {
                encabezado[0]: fila[0],
                encabezado[1]: int(fila[1]),
                encabezado[2]: float(fila[2]),
            }
            camion.append(registro)
    return camion


camion = leer_camion("../Data/camion.csv")
pprint(camion)
