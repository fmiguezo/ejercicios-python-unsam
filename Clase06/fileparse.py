# fileparse.py
# Ejercicio 6.6: Parsear un archivo CSV
# Ejercicio 6.7: Selector de Columnas
# Ejercicio 6.8: Conversión de tipo
# Ejercicio 6.9: Trabajando sin encabezados

import csv


def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    """
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers == True:
            encabezados = next(filas)
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
            if select:
                indices = [
                    encabezados.index(nombre_columna) for nombre_columna in select
                ]  # convierte los nombres de las columnas listadas en select a índices (posiciones) de columnas en el archivo
                encabezados = select
            else:
                indices = []

        registros = []
        for fila in filas:
            if not fila:  # Saltear filas vacías
                continue
            if has_headers == True:
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
            if types:
                # Determinar tipos si los especifíca
                fila = [func(val) for func, val in zip(types, fila)]

            if has_headers == True:
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
            else:
                # Armar la tupla
                registro = tuple(fila)
            registros.append(registro)

    return registros
