# camion.py
# Ejercicio 10.2: Iteración sobre objetos


class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter

        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
