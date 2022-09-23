# ticker.py
# Ejercicio 10.10: Un pipeline más largo
# Ejercicio 10.11: Filtremos los datos
# Ejercicio 10.12: El pipeline ensamblado
# Ejercicio 10.15: Código simple

from vigilante import vigilar
import csv
import informe_final
from formato_tabla import crear_formateador


def elegir_columnas(rows, indices):
    return ([row[index] for index in indices] for row in rows)


def cambiar_tipo(rows, types):
    return ([func(val) for func, val in zip(types, row)] for row in rows)


def hace_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ["nombre", "precio", "volumen"])
    return rows


def filtrar_datos(rows, nombres):
    return (row for row in rows if row["nombre"] in nombres)


def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    formateador = crear_formateador(fmt)
    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    formateador.encabezado(["Nombre", "Precio", "Volumen"])

    for row in rows:
        rowdata = [row["nombre"], str(row["precio"]), str(row["volumen"])]
        formateador.fila(rowdata)


if __name__ == "__main__":
    camion_file = "../Data/camion.csv"
    log_file = "../Data/mercadolog.csv"
    fmt = "txt"
    ticker(camion_file, log_file, fmt)
