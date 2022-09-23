# Ejercicio 1.17: Iteración sobre cadenas

cadena = "Ejemplo con for"
contador = 0

for c in cadena:
    print("caracter:", c)
    if c == "o":
        contador = contador + 1

print("Dentro del ciclo hay", contador, "letras O")
