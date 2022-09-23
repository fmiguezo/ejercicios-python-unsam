# Ejercicio 1.19: Métodos de cadenas
frutas = "Manzana,Naranja,Mandarina,Banana,Kiwi"
frutas.lower()

lowersyms = frutas.lower()
print(lowersyms)

frutas.find("Mandarina")

frutas[13:17]
print(frutas[13:17])

frutas = frutas.replace("Kiwi", "Melón")
print(frutas)

nombre = "   Naranja   \n"
nombre = nombre.strip()  # Remove surrounding whitespace
print(nombre)
