import csv
from pprint import pprint

#%% Precio pagado al productor
def leer_parque(nombre_archivo, parque):
    arboles_parque = parque
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        fila = filas
        lista_arboles = []
        for n_fila, fila in enumerate(filas, start=1):
            try:
                record = dict(zip(encabezados, fila))
                if record["espacio_ve"] == arboles_parque:
                    lista_arboles.append(record)
            except ValueError:
                print(f"Fila {n_fila}: No pude interpretar: {fila}")
        return lista_arboles


archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"
parque = "GENERAL PAZ"
arboles = leer_parque(archivo_arboles, parque)
