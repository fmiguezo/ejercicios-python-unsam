#%%
# Ejercicio 3.2. Función tiene_a(), nuevamente
# Errores: faltan ":" luego de la función y el while, el if dentro del while debería tener un == y no un =, y el return debería ser False y no Falso
# Comentario: además de esos errores, no evalúa las mayúsculas. Lo solucioné con un .lower() en la condición del while

##original
# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n
#         if expresion[i] = 'a'
#             return True
#         i += 1
#     return Falso

# tiene_a('UNSAM 2020')
# tiene_a('La novela 1984 de George Orwell')

##corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i].lower() == "a":
            return True
        i += 1
    return False


tiene_a("UNSAM 2020")
tiene_a("La novela 1984 de George Orwell")
