# Ejercicio 4.9: Consultas de datos
import csv
from pprint import pprint

#%%Leer camión /  Precio pagado al productor
def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        fila = filas
        camion = []
        for n_fila, fila in enumerate(filas, start=1):
            fila[1] = int(fila[1])
            fila[2] = float(fila[2])
            try:
                record = dict(zip(encabezados, fila))
                camion.append(record)
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

#%% 4.9
mas100 = [s for s in camion if s["cajones"] > 100]
myn = [s for s in camion if s["nombre"] in {"Mandarina", "Naranja"}]
costo10k = [s for s in camion if s["cajones"] * s["precio"] > 10000]
