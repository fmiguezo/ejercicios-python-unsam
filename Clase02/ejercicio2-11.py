import csv

f = open("../Data/camion.csv")
filas = csv.reader(f)
next(filas)
fila = next(filas)
print(fila)

t = (fila[0], int(fila[1]), float(fila[2]))
cost = t[1] * t[2]
print(cost)

print(f"{cost:0.2f}")

nombre, cajones, precio = t
print(nombre, cajones, precio)

t = (nombre, 2 * cajones, precio)
print(t)
