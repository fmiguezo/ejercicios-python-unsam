import csv

f = open("../Data/camion.csv")
filas = csv.reader(f)
next(filas)
fila = next(filas)
# print(fila)

d = {"nombre": fila[0], "cajones": int(fila[1]), "precio": float(fila[2])}

cost = d["cajones"] * d["precio"]
d["cajones"] = 75
d["fecha"] = (14, 8, 2020)
d["cuenta"] = 12345

# for k in d:
#     print(k, '=', d[k])

items = d.items()
# print(items)

for k, v in d.items():
    print(k, "=", v)

list(d)

claves = d.keys()
print(claves)

nuevos_items = [
    ("nombre", "Manzanas"),
    ("cajones", 100),
    ("precio", 490.1),
    ("fecha", (13, 8, 2020)),
]
print(nuevos_items)
d = dict(nuevos_items)
print(d)
