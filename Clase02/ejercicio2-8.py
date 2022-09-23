# def preguntar_edad(nombre):
#     edad = int(input(f'ingresá tu edad {nombre}: '))
#     if edad<0:
#         raise ValueError('La edad no puede ser negativa.')
#     return edad

# preguntar_edad('Florencia')

# for nombre in ['Pedro','Juan','Caballero']:
#     try:
#         edad = preguntar_edad(nombre)
#         print(f'{nombre} tiene {edad} años.')
#     except ValueError:
#         print(f'{nombre} no ingresó una edad válida.')


def costo_camion(nombre_archivo):
    f = open(nombre_archivo, "rt")
    headers = next(f).split(",")
    costo_total = 0
    try:
        for line in f:
            line = line.strip()
            row = line.split(",")
            row.pop(0)
            cantidad = int("".join(row[0]))
            precio = float("".join(row[1]))
            costo_cajon = cantidad * precio
            costo_total = costo_total + costo_cajon
        f.close()
        return costo_total
    except:
        print("Falta información")


costo = costo_camion("../Data/missing.csv")  # camion.csv
print("Costo total:", costo)
