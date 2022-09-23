# lote.py
# Ejercicio 9.1: Objetos como estructura de datos.
# Ejercicio 9.2: Agregá algunos métodos
# Ejercicio 9.3: Lista de instancias
# Ejercicio 9.4: Usá tu clase

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = int(cajones)
        self.precio = float(precio)
        
    def costo(self):
        return self.cajones * self.precio

    def vender(self,n):
        self.cajones -= n
