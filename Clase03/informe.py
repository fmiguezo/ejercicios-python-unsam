import csv
from pprint import pprint

#%% Precio pagado al productor
def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        fila = filas
        camion = []
        for n_fila, fila in enumerate(filas, start=1):
            try:
                record = dict(zip(encabezados, fila))
                camion.append(record)
            except ValueError:
                print(f"Fila {n_fila}: No pude interpretar: {fila}")
        return camion


archivo_camion = "../Data/camion.csv"
camion = leer_camion(archivo_camion)


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
archivo_camion = "../Data//fecha_camion.csv"
archivo_precios = "../Data/precios.csv"

camion = leer_camion(archivo_camion)
precios = leer_precios(archivo_precios)

costo_camion = 0
total_vendido = 0
for producto in camion:
    nombre = producto["nombre"]
    cajones = int(producto["cajones"])
    costo = float(producto["precio"])
    costo_camion += cajones * costo
    precio_venta = precios[nombre]
    total_vendido += cajones * precio_venta

balance = total_vendido - costo_camion

print("*" * 22)
print(" * BALANCE VERDULERÍA *")
print("*" * 22)
print(
    f"Costo camion: {costo_camion:.2f}\nVenta: {total_vendido:.2f}\nBalance: {balance:.2f}"
)

# salida
# Fila 30: No pude interpretar: []
# **********************
#  * BALANCE VERDULERÍA *
# **********************
# Costo camion: 47671.15
# Venta: 62986.10
# Balance: 15314.95
