def buscar_precio(producto):
    f = open("../Data/precios.csv", "rt")
    headers = next(f).split(",")
    mensaje = ""

    for line in f:
        line = line.strip()  # sacar el espacio vacío del final
        row = line.split(",")  # convertir lineas en array
        if row[0] == producto:
            return print("El precio de un cajón de", producto, "es", row[1])

    if producto not in row:
        return print(producto, "no figura en la lista de precios")

    f.close()


buscar_precio("Frambuesa")

"""
buscar_precio('Kale')
salida:
Kale no se encuentra en la lista de precios

buscar_precio('Naranja')
salida:
El precio de un cajón Naranja es 106.28

buscar_precio('Frambuesa')
salida:
El precio de un cajón de Frambuesa es 34.25
"""
