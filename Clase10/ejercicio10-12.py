# ticker.py
# Ejercicio 10.12: El pipeline ensamblado

from vigilante import vigilar
import csv
import informe_final
from formato_tabla import crear_formateador


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ["nombre", "precio", "volumen"])
    return rows


def filtrar_datos(rows, nombres):
    for row in rows:
        if row["nombre"] in nombres:
            yield row


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
