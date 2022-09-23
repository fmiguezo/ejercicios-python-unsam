#%%
# Ejercicio 3.3. Función tiene_uno()
# Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
# tiene_uno(1984) #da error porque el tipo 'int' no tiene len, hay que convertir la expresion a un string
# Lo solucioné agregando "expresion = str(expresion)" a la primera línea de la función

## original
# def tiene_uno(expresion):
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#         i += 1
#     return tiene


# tiene_uno('UNSAM 2020')
# tiene_uno('La novela 1984 de George Orwell')
# tiene_uno(1984) #da error porque el tipo 'int' no tiene len


## corregido
def tiene_uno(expresion):
    expresion = str(expresion)  # esta es la línea que agregué
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == "1":
            tiene = True
        i += 1
    return tiene


tiene_uno("UNSAM 2020")
tiene_uno("La novela 1984 de George Orwell")
tiene_uno(1984)
