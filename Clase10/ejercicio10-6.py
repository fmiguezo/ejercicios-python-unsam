# vigilante.py
# Ejercicio 10.6: Uso de un generador para producir datos

import os
import time


def vigilar(nombre_archivo):
    f = open(nombre_archivo)
    f.seek(0, os.SEEK_END)  # Mover el índice 0 posiciones desde el EOF

    while True:
        line = f.readline()
        if line == "":
            time.sleep(0.5)  # Esperar un rato y
            continue  # vuelve al comienzo del while
        else:
            yield line


def f_principal(argumentos):
    vigilador = vigilar(argumentos)
    vigilador.__next__()


if __name__ == "__main__":
    for line in vigilar("../Data/mercadolog.csv"):
        fields = line.split(",")
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if volumen > 1000:
            print(f"{nombre:>10s} {precio:>10.2f} {volumen:>10d}")
