# Ejercicio 10.3: Un iterador adecuado


class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def __len__(self):
        return len(self.lotes)

    def __getitem__(self, a):
        return self.lotes.__getitem__(a)

    def __str__(self):
        camion = []
        for l in self.lotes:
            lote = f"Lote de {l.cajones} cajones de {l.nombre}, pagados a ${l.precio} cada uno."
            camion.append(lote)
        s = "\n".join(l for l in camion)
        return f"Camion con {self.__len__()} lotes:\n{s}"

    def __repr__(self):
        s = ", ".join([object.__str__(i) for i in self.lotes])
        return f"Camion([{s}])"

    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter

        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
