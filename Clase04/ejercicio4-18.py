# Ejercicio 4.18: Diccionario con medidas
#%%
import csv


def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = [headers.index(ncolumna) for ncolumna in headers]
        row = next(rows)
        arboleda = [
            {ncolumna: row[index] for ncolumna, index in zip(headers, indices)}
            for row in rows
        ]
        return arboleda


def medidas_de_especies(especies, arboleda):
    dic = {
        x: [
            (float(arbol["altura_tot"]), float(arbol["diametro"]))
            for arbol in arboleda
            if arbol["nombre_com"] == x
        ]
        for x in especies
    }
    # for x in especies:
    #     dic[x] = [
    #     (float(arbol["altura_tot"]), float(arbol["diametro"]))
    #     for arbol in arboleda
    #     if arbol["nombre_com"] == x]
    return dic


archivo_arboles = "../Data/arbolado-en-espacios-verdes.csv"
arboleda = leer_arboles(archivo_arboles)
especies = ["Eucalipto", "Palo borracho rosado", "Jacarandá"]

medidas_de_especies(especies, arboleda)

##salida
"""
{'Eucalipto': [(20.0, 40.0),
  (20.0, 40.0),
  (20.0, 40.0),
  (20.0, 40.0),
  (20.0, 40.0),
  (20.0, 40.0),
    ...],
 'Palo borracho rosado': [(10.0, 50.0),
  (10.0, 50.0),
  (10.0, 50.0),
  (2.0, 4.0),
  (2.0, 4.0),
  (2.0, 4.0),
  (2.0, 4.0),
  (2.0, 4.0),
  (2.0, 4.0),
    ...],
 'Jacarandá': [(5.0, 10.0),
  (5.0, 10.0),
  (5.0, 10.0),
  (5.0, 10.0),
  (5.0, 10.0),
  (5.0, 10.0),
  (5.0, 10.0),
  (5.0, 10.0),
  (5.0, 10.0),
  (5.0, 10.0),
    ...]}
"""
