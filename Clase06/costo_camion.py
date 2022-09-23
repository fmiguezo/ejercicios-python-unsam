# costo_camion.py
# Ejercicio 6.12: Un poco más allá
import informe_funciones

#%%
def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion(nombre_archivo)
    costo_total = 0
    for producto in camion:
        ncajones = producto["cajones"]
        precio = producto["precio"]
        costo_total += ncajones * precio
    return costo_total


#%%
def main():
    costo = costo_camion("../Data/camion.csv")
    return costo
