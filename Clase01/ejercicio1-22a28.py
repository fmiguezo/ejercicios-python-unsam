# Ejercicio 1.22: Extracción y reasignación de elementos.
frutas = "Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera"
lista_frutas = frutas.split(",")
lista_frutas[0]
lista_frutas[1]
lista_frutas[-1]
lista_frutas[-2]
lista_frutas[2] = "Granada"
lista_frutas[0:3]
lista_frutas[-2:]

compra = []
compra.append("Pera")

lista_frutas[-2:] = compra
print(lista_frutas)

# Ejercicio 1.23: Ciclos sobre listas
for s in lista_frutas:
    print("s =", s)

# Ejercicio 1.24: Test de pertenencia
"Granada" in lista_frutas
"Lima" in lista_frutas
"Limon" not in lista_frutas

# Ejercicio 1.25: Adjuntar, insertar y borrar elementos
lista_frutas.append("Mango")
lista_frutas.insert(1, "Lima")
lista_frutas.remove("Mandarina")
lista_frutas.append("Banana")
lista_frutas.count("Banana")
lista_frutas.remove("Banana")

# Ejercicio 1.26: Sorting
lista_frutas.sort()
lista_frutas.sort(reverse=True)

# Ejercicio 1.27: Juntar múltiples cadenas
lista_frutas = ["Banana", "Mango", "Frambuesa", "Pera", "Granada", "Manzana", "Lima"]
a = ",".join(lista_frutas)
print(a)
b = ":".join(lista_frutas)
print(b)
c = "".join(lista_frutas)
print(c)

# Ejercicio 1.28: Listas de cualquier cosa
nums = [101, 102, 103]
items = ["spam", lista_frutas, nums]
print(items)
items[0]
items[0][0]
items[1]
items[1][1]
items[1][1][2]
items[2]
items[2][1]
