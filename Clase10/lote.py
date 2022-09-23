# lote.py
# Ejercicio 9.1: Objetos como estructura de datos.
# Ejercicio 9.2: Agregá algunos métodos
# Ejercicio 9.3: Lista de instancias
# Ejercicio 9.4: Usá tu clase
# Ejercicio 9.9: Mejor salida para
# Ejercicio 10.3: Un iterador adecuado


class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = str(nombre)
        self.cajones = int(cajones)
        self.precio = float(precio)

    def __iter__(self):
        return self.lotes.__iter__()

    def __repr__(self):
        return f"Lote({self.nombre}, {self.cajones}, {self.precio})"

    def costo(self):
        return self.cajones * self.precio

    def vender(self, n):
        self.cajones -= n
