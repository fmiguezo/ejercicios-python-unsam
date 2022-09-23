# Ejercicio 8.5: Recorrer el árbol de archivos
import os
import sys


def archivos_png(directorio):
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name.endswith(".png"):
                print(os.path.join(name))


def f_principal(argv):
    archivos_png("../Data/ordenar")


if __name__ == "__main__":
    f_principal(sys.argv)
