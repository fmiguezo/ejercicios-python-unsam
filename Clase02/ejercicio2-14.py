def diccionarioGeringoso(lista):
    diccionario = {}
    capadepenapa = ""

    for palabra in range(len(lista)):  # itero la lista para traducir 1x1
        palabra_lista = lista[palabra]

        for c in palabra_lista:
            capadepenapa += c  # porque siempre agrego c, así me ahorro el else
            if (
                c in "aeiou"
            ):  # si el caracter c está entre aeiou, es para substrings (el caracter es una subcadena del conjunto de caracteres)
                capadepenapa += "p" + c
            if c in "AEIOU":
                capadepenapa += "P" + c
        diccionario.update(
            {lista[palabra]: capadepenapa}
        )  # agrego las palabras al diccionario
        capadepenapa = ""  # limpio la cadena geringosa para que arranque vacía en la próxima iteración
    print(diccionario)


lista = ["banana", "manzana", "mandarina"]
diccionarioGeringoso(lista)
