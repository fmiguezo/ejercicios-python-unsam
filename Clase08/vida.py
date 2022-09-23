# vida.py
# Ejercicio 8.1: Segundos vividos

import datetime
import sys


def vida_en_segundos(fecha_nac):
    fecha_nac_conv = datetime.datetime.strptime(fecha_nac, "%d/%m/%Y")
    hoy = datetime.datetime.now()
    diferencia = hoy - fecha_nac_conv
    seg_vividos = diferencia.total_seconds()
    return seg_vividos


def f_principal(argv):
    fecha_nac = "05/07/1990"
    vida_en_segundos(fecha_nac)


if __name__ == "__main__":
    f_principal(sys.argv)
