import csv
from pprint import pprint
from collections import Counter

#%% Precio pagado al productor
# ej 3.18
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
                if record["espacio_ve"] == arboles_parque or arboles_parque == "":
                    lista_arboles.append(record)
                else:
                    pass
            except ValueError:
                print(f"Fila {n_fila}: No pude interpretar: {fila}")
        return lista_arboles


##salida => imprime los 690 árboles de 'GENERAL PAZ'
#%%
# ej 3.19
def especies(lista_arboles):
    lista_especies = set([])
    for fila in lista_arboles:
        especie = fila["nombre_com"]
        lista_especies.add(especie)
    return lista_especies


##salida
"""
{'Acacia blanca',
 'Acacia negra',
 'Alcanforero',
 'Arce negundo',
 'Bunya-bunya (Araucaria de Bidwill)',
 'Caqui',
 'Casuarina',
 'Cedrela',
 'Cedro',
 'Cedro de San Juan',
 'Cedro del Atlas (Cedro plateado o Cedro atlántico)',
 'Cedro del Himalaya',
 'Cedro del Himalaya variedad aurea',
 'Ceibo',
 'Chamaecyparis',
 'Ciprés',
 'Ciprés blanco',
 'Ciprés calvo',
 'Ciprés leylandi',
 'Corona de cristo',
 'Criptomeria (Cedro del Japón)',
 'Eucalipto',
 'Falso Guayabo (Guayaba del Brasil)',
 'Fenix',
 'Ficus',
 'Fotinia',
 'Fresno (Fresno común)',
 'Fresno americano',
 'Ginkgo',
 'Jacarandá',
 'Juniperus',
 'Lapacho rosado',
 'Laurel de jardin (Laurel de flor)',
 'Laurus',
 'Libocedro (Calocedro)',
 'Ligustro',
 'Ligustro disciplinado (Ligustro variegado)',
 'Limpiatubos',
 'Liquidambar',
 'Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert)',
 'Magnolia',
 'Morera blanca',
 'Morera de papel (Moral de China)',
 'Morera negra',
 'No Determinable',
 'No Determinado',
 'Nogal europeo (Nogal común)',
 'Níspero japonés',
 'Olea',
 'Olivo',
 'Olivo oloroso',
 'Olmo',
 'Olmo europeo',
 'Ombú',
 'Palma Bangalow  (Palma Rey)',
 'Palma de california',
 'Palmito',
 'Palo borracho rosado',
 'Paraíso',
 'Pindó',
 'Pino',
 'Pino carrasco (Pino de Jerusalén)',
 'Pino de las canarias',
 'Pino del Paraná (Pino de Misiones o Pino de Brasil)',
 'Plátano',
 'Roble',
 'Roble americano',
 'Roble común',
 'Roble sedoso (Grevillea)',
 'Sauce eléctrico',
 'Tilo',
 'Timbó (Oreja de negro)',
 'Tipa blanca',
 'Tuja',
 'Tuya oriental',
 'Visco (Viscote, Arca)',
 'Washingtonia',
 'Washingtonia (Palmera washingtonia)',
 'Álamo blanco piramidal',
 'Álamo negro',
 'Árbol del cielo (Ailanto o Árbol de los dioses)'}"""
#%%
def contar_ejemplares(lista_arboles):
    cantidad_ejemplares = Counter()
    for fila in lista_arboles:
        cantidad_ejemplares[fila["nombre_com"]] += 1
    return cantidad_ejemplares


#%%
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for fila in lista_arboles:
        if especie == fila["nombre_com"]:
            altura = float(fila["altura_tot"])
            alturas.append(altura)
    maximo = max(alturas)
    promedio = round(sum(alturas) / len(alturas), 2)
    return maximo, promedio


#%%
parque = "GENERAL PAZ"
archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"
lista_arboles = leer_parque(archivo_arboles, parque)
lista_especies = especies(lista_arboles)

#%%
# 20
print("------TABLA EJ.20------")
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
    for fila in matriz:
        print(f"{fila[i]:<30s}", end="")
    print("")
print("")
##salida
# ------TABLA EJ.20------
# General Paz                   Los Andes                     Centenario
# Casuarina: 97                 Jacarandá: 117                Plátano: 137
# Tipa blanca: 54               Tipa blanca: 28               Jacarandá: 45
# Eucalipto: 49                 Ciprés: 21                    Tipa blanca: 42
# Palo borracho rosado: 44      Palo borracho rosado: 18      Palo borracho rosado: 41
# Fenix: 40                     Lapacho: 12                   Fresno americano: 38

#%%
##ej 3.21
print("------TABLA EJ.21------")
parques = ["GENERAL PAZ", "ANDES, LOS", "CENTENARIO"]
max_prom = []
for x in range(0, len(parques)):
    parque = parques[x]
    arboles = leer_parque(archivo_arboles, parque)
    especie = "Jacarandá"
    alturas = obtener_alturas(arboles, especie)
    max_prom.append(alturas)

headers = ("Medida", "General Paz", "Los Andes", "Centenario")
columna = ("max", "prom")
print(f"{headers[0]:<20s}{headers[1]:<20s}{headers[2]:<20s}{headers[3]:<20s}")
for x in range(0, 2):
    print(f"{columna[x]:<20s}", end="")
    for y in range(len(max_prom)):
        print(f"{max_prom[y][x]:<20}", end="")
    print("")

##salida
# ------TABLA EJ.21------
# Medida              General Paz         Los Andes           Centenario
# max                 16.0                25.0                18.0
# prom                10.2                10.54               8.96


##ej 3.22
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for fila in lista_arboles:
        if especie == fila["nombre_com"]:
            inclinacion = int(fila["inclinacio"])
            inclinaciones.append(inclinacion)
    return inclinaciones


parque = ""
archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"
lista_arboles = leer_parque(archivo_arboles, parque)
especie = "Jacarandá"
lista_inclinacion = obtener_inclinaciones(lista_arboles, especie)

##salida => imprime todas las inclinaciones de la especie seleccionada
