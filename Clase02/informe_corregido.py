import csv
from pprint import pprint

#%% Precio pagado al productor
def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        for line in rows:
            d = {"nombre": line[0], "cajones": int(line[1]), "precio": float(line[2])}
            camion.append(d)
        return camion


#%% Precio de venta
def leer_precios(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows = csv.reader(f)
        diccionario = {}
        for i, row in enumerate(rows):
            try:
                diccionario[row[0]] = float(row[1])
            except IndexError:
                print(f"Ups! no logro entender la línea {i+1}:{row}")
        return diccionario


#%%
archivo_camion = "../Data/camion.csv"
archivo_precios = "../Data/precios.csv"

camion = leer_camion(archivo_camion)
precios = leer_precios(archivo_precios)

costo_camion = 0
total_vendido = 0
for producto in camion:
    nombre = producto["nombre"]
    cajones = producto["cajones"]
    costo = producto["precio"]
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
