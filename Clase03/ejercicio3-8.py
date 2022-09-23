import csv


def costo_camion(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        costo_total = 0
        for i, fila in enumerate(f):  # for n_fila, fila in enumerate(filas, start=1):
            try:
                i += 1
                fila = fila.strip()
                row = fila.split(",")
                cajones = int(row[1])
                costo = float(row[2])
                costo_total += cajones * costo
            except ValueError:
                print(f"Fila {i}: No pude interpretar: {fila}")
        return costo_total


cost = costo_camion("../Data/missing.csv")
