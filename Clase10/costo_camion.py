#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# costo_camion.py

#%% ejercicio 7.5
# Ejercicio 9.4: Usá tu clase
# Ejercicio 10.2: Iteración sobre objetos

import informe_final


def costo_camion(nombre_archivo):
    """
    Computa el precio total (cantidad * precio) de un archivo camion
    """
    camion = informe_final.leer_camion(nombre_archivo)
    return camion.precio_total()


def f_principal(argumentos):
    costo = costo_camion(argumentos[1])
    # costo_camion.costo_camion('../Data/camion.csv')
    print(f"Costo total: {costo}")


#%%
if __name__ == "__main__":
    import sys

    f_principal(sys.argv)
