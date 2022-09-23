# costo_camion.py
# Ejercicio 6.12: Un poco más allá
# Ejercicio 7.4: Función principal
# Ejercicio 7.5: Hacer un script

import informe_final
import sys

#%%
def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo)
    costo_total = 0
    for producto in camion:
        ncajones = producto["cajones"]
        precio = producto["precio"]
        costo_total += ncajones * precio
    print("Costo total:", costo_total)
    return


#%% Función Principal
def f_principal(argv):
    if len(argv) != 2:
        raise SystemExit(f"Uso adecuado: {argv[0]} " "archivo_camion")
    else:
        camion = argv[1]
        costo_camion(camion)


if __name__ == "__main__":
    f_principal(sys.argv)
