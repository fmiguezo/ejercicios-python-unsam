# Ejercicio 6.4: Estructurar un programa como una colección de funciones

import csv

#%% Precio pagado al productor
def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        fila = filas
        camion = []
        for n_fila, fila in enumerate(filas, start=1):
            try:
                record = dict(zip(encabezados, fila))
                camion.append(record)
            except ValueError:
                print(f"Fila {n_fila}: No pude interpretar: {fila}")
        return camion


#%% Precio de venta
def leer_precios(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        filas = csv.reader(f)
        precios = {}
        for n_fila, fila in enumerate(filas):
            try:
                precios[fila[0]] = float(fila[1])
            except IndexError:
                # print(f"Fila {n_fila}: No pude interpretar: {fila}")
                pass
        return precios


#%% Armar informe
def hacer_informe(camion, precio):
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


camion = leer_camion("../Data/camion.csv")
precios = leer_precios("../Data/precios.csv")
informe = hacer_informe(camion, precios)
imprimir_informe(informe)


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
