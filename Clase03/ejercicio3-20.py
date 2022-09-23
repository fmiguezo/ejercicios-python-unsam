import csv
from pprint import pprint
from collections import Counter

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


def especies(lista_arboles):
    lista_especies = set([])
    for fila in lista_arboles:
        especie = fila["nombre_com"]
        lista_especies.add(especie)
    return lista_especies


def contar_ejemplares(lista_arboles):
    cantidad_ejemplares = Counter()
    for fila in lista_arboles:
        cantidad_ejemplares[fila["nombre_com"]] += 1
    return cantidad_ejemplares


archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"

parques = ["GENERAL PAZ", "ANDES, LOS", "CENTENARIO"]
matriz = []
for x in range(0, len(parques)):
    parque = parques[x]
    arboles = leer_parque(archivo_arboles, parque)
    lista_especies = especies(arboles)
    cantidad_ejemplares = contar_ejemplares(arboles)
    cinco_mas_comunes = contar_ejemplares(arboles).most_common(5)
    array = []
    for x in range(0, len(cinco_mas_comunes)):
        for y in range(0, 1):
            arbol = f"{cinco_mas_comunes[x][y]}: {cinco_mas_comunes[x][1]}"
            array.append(arbol)
    matriz.append(array)

headers = ("General Paz", "Los Andes", "Centenario")
print(f"{headers[0]:<30s}{headers[1]:<30s}{headers[2]:<30s}")
for i in range(0, 5):
    print("")
    for fila in matriz:
        print(f"{fila[i]:<30s}", end="")
