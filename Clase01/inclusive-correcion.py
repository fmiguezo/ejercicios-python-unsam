frase = "todos somos programadores"
palabras = frase.split()  # split separa la cadena en subcadenas separadas por espacios
traduccion = []

for palabra in palabras:
    print(palabra)
    if palabra[-1] == "o":
        nueva_palabra = palabra[:-1] + "e"
    elif len(palabra) > 1 and palabra[-2] == "o":
        nueva_palabra = palabra[:-2] + "e" + palabra[-1]
    else:
        nueva_palabra = palabra
    traduccion.append(nueva_palabra)

frase_t = " ".join(traduccion)
print(frase_t)
