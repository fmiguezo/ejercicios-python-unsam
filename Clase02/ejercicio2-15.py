import csv

# def costo_camion(nombre_archivo):
#     '''Computa el precio total del camion (cajones * precio) de un archivo'''
#     total = 0.0

#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             ncajones = int(row[1])
#             precio = float(row[2])
#             total += ncajones * precio
#     return total


def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)

    return camion


camion = leer_camion("../Data/camion.csv")

print(camion)
print(camion[0])
print(camion[1])
print(camion[1][1])

total = 0.0
for s in camion:
    total += s[1] * s[2]

print(total)

total = 0.0
for nombre, cajones, precio in camion:
    total += cajones * precio

print(total)
