# Ejercicio 1.18: Geringoso rústico

cadena = "Geringoso"
capadepenapa = ""
for c in cadena:
    if c == "a":
        capadepenapa = capadepenapa + "apa"
    elif c == "e":
        capadepenapa = capadepenapa + "epe"
    elif c == "i":
        capadepenapa = capadepenapa + "ipi"
    elif c == "o":
        capadepenapa = capadepenapa + "opo"
    elif c == "u":
        capadepenapa = capadepenapa + "upu"
    else:
        capadepenapa = capadepenapa + c

print(cadena, "en geringoso se dice", capadepenapa)
