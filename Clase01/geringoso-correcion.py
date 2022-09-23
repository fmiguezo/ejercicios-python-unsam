cadena = "Geringoso"
capadepenapa = ""

# # solucion mala
# for c in cadena:
#     if c == "a":
#         capadepenapa += "apa"
#     elif c == "e":
#         capadepenapa += "epe"
#     elif c == "i":
#         capadepenapa += "ipi"
#     elif c == "o":
#         capadepenapa += "opo"
#     elif c == "u":
#         capadepenapa += "upu"
#     else:
#         capadepenapa += c

#     print(capadepenapa)

# solucion mejor, se puede poner el lower también
for c in cadena:
    capadepenapa += c  # porque siempre agrego c, así me ahorro el else
    if (
        c in "aeiou"
    ):  # si el caracter c está entre aeiou, es para substrings (el caracter es una subcadena del conjunto de caracteres)
        capadepenapa += "p" + c
    if c in "AEIOU":
        capadepenapa += "P" + c
    print(capadepenapa)
