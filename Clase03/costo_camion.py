import csv


def costo_camion(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf8") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        fila = filas
        costo_total = 0
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record["cajones"])
                precio = float(record["precio"])
                costo_total += ncajones * precio
            # Esto atrapa errores en los int() y float() de arriba.
            except ValueError:
                print(f"Fila {n_fila}: No pude interpretar: {fila}")
        return costo_total


cost = costo_camion("../Data/fecha_camion.csv")
