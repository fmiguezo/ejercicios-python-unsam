# Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo
"""Queremos hacer un traductor que cambie las palabras masculinas de una frase 
por su versión neutra. Como primera aproximación, completá el siguiente código 
para reemplazar todas las letras 'o' que figuren en el último o anteúltimo 
caracter de cada palabra por una 'e'. Por ejemplo 'todos somos programadores' 
pasaría a ser 'todes somes programadores'. Guardá tu código en el archivo 
inclusive.py
Probá tu código con 'Los hermanos sean unidos porque ésa es la ley primera', 
'¿cómo transmitir a los otros el infinito Aleph?' y 'Todos, tu también'. 
¿Qué falla en esta última? (¡no hace falta que lo resuelvas!)
"""
frase = "Todos, tu también"
palabras = frase.split()
lista_palabras = []

for palabra in palabras:
    if len(palabra) > 1:
        if palabra[-1] == "o":
            palabra = palabra[:-1] + palabra[-1].replace("o", "e")
        if palabra[-2] == "o":
            palabra = palabra[:-2] + palabra[-2].replace("o", "e") + palabra[-1]
        if (palabra[-1] == ",") | (palabra[-1] == ".") | (palabra[-1] == "?"):
            if palabra[-2] == "o":
                palabra = palabra[:-2] + palabra[-2].replace("o", "e")
            if palabra[-3] == "o":
                palabra = (
                    palabra[:-3]
                    + palabra[-3].replace("o", "e")
                    + palabra[-2]
                    + palabra[-1]
                )
    else:
        palabra = palabra
    lista_palabras.append(palabra)

frase_t = " ".join(lista_palabras)
print(frase_t)
