f = open("../Data/precios.csv", "rt")
headers = next(f).split(",")

for line in f:
    line = line.strip()
    row = line.split(",")
    if row[0] == "Naranja":
        print("El precio de la naranja es", row[1])

f.close()
