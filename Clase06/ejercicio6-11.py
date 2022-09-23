# Ejercicio 6.11: Usemos tu módulo
import fileparse

#%% Precio pagado al productor
def leer_camion(nombre_archivo):
    camion = fileparse.parse_csv(
        nombre_archivo, select=["nombre", "cajones", "precio"], types=[str, int, float]
    )
    return camion


#%% Precio de venta
def leer_precios(nombre_archivo):
    lista_precios = fileparse.parse_csv(
        nombre_archivo, types=[str, float], has_headers=False
    )
    precios = dict(lista_precios)
    return precios


#%% Armar informe
def hacer_informe(camion, precios):
    lista_tpl = []
    for producto in camion:
        nombre = producto["nombre"]
        cajones = int(producto["cajones"])
        costo = float(producto["precio"])
        precio_venta = precios[nombre]
        tpl = (nombre, cajones, costo, (precio_venta - costo))
        lista_tpl.append(tpl)
    return lista_tpl


#%% Imprimir informe
def imprimir_informe(informe):
    headers = ("Nombre", "Cajones", "Precio", "Cambio")
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(f'{"-"*10:>10s} {"-"*10:>10s} {"-"*10:>10s} {"-"*10:>10s}')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d} {"$"+str(precio):>10} {cambio:>10.2f}')
    return


#%% Ejecutar
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)
    return


def main():
    informe_camion("../Data/camion.csv", "../Data/precios.csv")


##salida
"""
    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84
"""
