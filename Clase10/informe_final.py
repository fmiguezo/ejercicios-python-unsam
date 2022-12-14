#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

#%% ejercicio 7.7
# Ejercicio 9.4: Usá tu clase
# Ejercicio 9.5: Un problema de extensibilidad
# Ejercicio 9.6: Usemos herencia para cambiar la salida
# Ejercicio 9.7: Polimorfismo en acción
# Ejercicio 9.8: Volvamos a armar todo
# Ejercicio 10.2: Iteración sobre objetos


import fileparse
import lote
import formato_tabla
from camion import Camion


def leer_camion(nombre_archivo):
    """
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    """
    with open(nombre_archivo) as file:
        camiondicts = fileparse.parse_csv(
            file, select=["nombre", "cajones", "precio"], types=[str, int, float]
        )

    camion = [lote.Lote(d["nombre"], d["cajones"], d["precio"]) for d in camiondicts]
    return Camion(camion)


def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    return dict(precios)


def hacer_informe(camion, precios):
    lista = []
    for c in camion:
        cambio = precios[c.nombre] - c.precio
        t = (c.nombre, c.cajones, c.precio, cambio)
        lista.append(t)
    return lista


def imprimir_informe(data_informe, formateador):
    """
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia)
    """
    formateador.encabezado(["Nombre", "Cantidad", "Precio", "Cambio"])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f"${precio:0.2f}", f"{cambio:0.2f}"]
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt="txt"):
    """
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    """
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)


#%%
def f_principal(argumentos, fmt="txt"):
    # informe_camion(argumentos[1], argumentos[2], fmt)
    informe_camion("../Data/camion.csv", "../Data/precios.csv")


if __name__ == "__main__":
    import sys

    f_principal(sys.argv)
