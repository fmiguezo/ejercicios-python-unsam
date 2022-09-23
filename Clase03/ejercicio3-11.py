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

from collections import Counter

tenencias = Counter()

for s in camion:
    tenencias[s["nombre"]] += int(s["cajones"])

tenencias["Naranja"]
# Las 3 frutas con más cajones
tenencias.most_common(3)

camion2 = leer_camion("../Data/camion2.csv")
tenencias2 = Counter()
for s in camion2:
    tenencias2[s["nombre"]] += int(s["cajones"])

combinada = tenencias + tenencias2
