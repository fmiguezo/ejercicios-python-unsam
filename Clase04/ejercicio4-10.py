# Ejercicio 4.10: Extracción de datos
import csv
from pprint import pprint

#%%Leer camión /  Precio pagado al productor
def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        fila = filas
        camion = []
        for n_fila, fila in enumerate(filas, start=1):  # itera las filas del archivo
            fila[1] = int(fila[1])  # parsea a int
            fila[2] = float(fila[2])  # parsea a float
            try:
                record = dict(zip(encabezados, fila))  # arma diccionario
                camion.append(record)  # agrega a la lista de diccionarios
            except ValueError:
                print(f"Fila {n_fila}: No pude interpretar: {fila}")
        return camion


#%% Precio de venta
def leer_precios(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        filas = csv.reader(f)
        precios = {}
        for n_fila, fila in enumerate(filas):
            try:
                precios[fila[0]] = float(fila[1])
            except IndexError:
                print(f"Fila {n_fila}: No pude interpretar: {fila}")
        return precios


#%%
archivo_camion = "../Data/camion.csv"
archivo_precios = "../Data/precios.csv"

camion = leer_camion(archivo_camion)
precios = leer_precios(archivo_precios)

costo = sum([s["cajones"] * s["precio"] for s in camion])
valor = sum([s["cajones"] * precios[s["nombre"]] for s in camion])
balance = valor - costo

# print(
#     f"Costo camion: {costo:.2f}\nVenta: {valor:.2f}\nBalance: {balance:.2f}"
# )

# ej 4.10
nombre_cajones = [(s["nombre"], s["cajones"]) for s in camion]
nombres = {s["nombre"] for s in camion}
stock = {nombre: 0 for nombre in nombres}
for s in camion:
    stock[s["nombre"]] += s["cajones"]
camion_precios = {nombre: precios[nombre] for nombre in nombres}
