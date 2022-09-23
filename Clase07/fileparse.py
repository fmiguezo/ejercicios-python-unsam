# fileparse.py
# Ejercicio 6.6: Parsear un archivo CSV
# Ejercicio 6.7: Selector de Columnas
# Ejercicio 6.8: Conversión de tipo
# Ejercicio 6.9: Trabajando sin encabezados
# Ejercicio 7.1: Lancemos excepciones
# Ejercicio 7.2: Atrapemos excepciones
# Ejercicio 7.6: De archivos a "objetos cual archivos"

import csv


def parse_csv(lineas, select=None, types=None, has_headers=True, silence_errors=False):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    """
    filas = csv.reader(lineas, delimiter=",")

    if (select != None) & (has_headers == False):
        raise RuntimeError("Para seleccionar, necesito encabezados.")

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
    for i, fila in enumerate(filas):
        if not fila:  # Saltear filas vacías
            continue
        if has_headers == True:
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
        if types:
            try:
                # Determinar tipos si los especifíca
                fila = [func(val) for func, val in zip(types, fila)]
            except ValueError as e:
                if silence_errors == False:
                    print(f"Fila {i+1}: No pude convertir {fila}")
                    print(f"Fila {i+1}: Motivo", e)

        if has_headers == True:
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
        else:
            # Armar la tupla
            registro = tuple(fila)
        registros.append(registro)

    return registros
