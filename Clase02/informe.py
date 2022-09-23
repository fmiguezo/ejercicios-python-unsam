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

total_camion = 0.0
for s in camion:
    total_camion += s["cajones"] * s["precio"]
print("El costo del camión fue de ${total_camion}".format(total_camion=total_camion))


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

# calcular la cantidad de cajones por producto
def cajones_camion(nombre_archivo):
    cajones = {}

    with open(nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            if (
                row[0] not in cajones
            ):  # para que no pise el valor si la key está duplicada
                cajones[row[0]] = int(row[1])
            else:
                cajones[row[0]] = (
                    int(row[1]) + cajones[row[0]]
                )  # si la key está duplicada, suma el valor original con el de la nueva línea
    return cajones


cajones = cajones_camion("../Data/camion.csv")

# total de cajones comprados x el precio de venta
total_venta = 0.0
for s in cajones:
    total_venta += cajones[s] * precios[s]
print("El total de la venta fue de ${total_venta}".format(total_venta=total_venta))

if total_venta > total_camion:
    print(
        "Hubo una ganancia de ${ganancia}".format(
            ganancia=round(total_venta - total_camion, 2)
        )
    )
elif total_camion < total_venta:
    print(
        "Hubo una pérdida de ${perdida}".format(
            perdida=round(total_camion - total_venta, 2)
        )
    )
else:
    print("No hubo ni pérdida ni ganancia")
