#%%
# Ejercicio 3.4. Alcances
# Comentario: a la función le falta el return por eso no devuelve ningún valor, le agregué el "return c" en la última línea para que devuelva el valor de c

## original
# def suma(a,b):
#     c = a + b

# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")


def suma(a, b):
    c = a + b
    return c


a = 2
b = 3
c = suma(a, b)
print(f"La suma da {a} + {b} = {c}")
