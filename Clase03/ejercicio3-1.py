# Ejercicio 3.1. Función tiene_a()
# Comentario: En el caso #1 y #3 da False cuando debería ser True.
# El error es que para las palabras que no empiezan con "a", el while retorna falso y termina la ejecución, no sigue buscando en las demás letras del string.
#    Lo corregí sacando el else del while, y poniendo un "return False" fuera del while, para que retorne falso si la oración no tiene a. Agregué un .lower() a la condición del while para que convierta las mayúsculas a minúsculas, para que tome las "A" como True
#    A continuación va el código corregido

# #Original
# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         else:
#             return False
#         i += 1

# tiene_a('UNSAM 2020') #False
# tiene_a('abracadabra') #True
# tiene_a('La novela 1984 de George Orwell') #False

# Corregido
def tiene_a(expresion):
    n = len(expresion)
    print(n)
    i = 0
    while i < n:
        if expresion[i].lower() == "a":
            return True
        i += 1
    return False


tiene_a("UNSAM 2020")  # True
tiene_a("abracadabra")  # True
tiene_a("La novela 1984 de George Orwell")  # True
