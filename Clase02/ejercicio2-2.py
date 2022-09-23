f = open("../Data/camion.csv", "rt")
headers = next(f).split(",")
costo_total = 0

for line in f:
    line = line.strip()
    row = line.split(",")
    row.pop(0)
    cantidad = int("".join(row[0]))
    precio = float("".join(row[1]))
    costo_cajon = cantidad * precio
    costo_total = costo_total + costo_cajon
f.close()

print("Costo total", costo_total)
