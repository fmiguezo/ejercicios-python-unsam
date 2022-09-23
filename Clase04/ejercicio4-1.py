# ejercición 4.1

# original
# def invertir_lista(lista):
#     '''Recibe una lista L y la develve invertida.'''
#     invertida = []
#     i = len(lista)
#     while i > 0:    # tomo el último elemento
#         i = i-1
#         invertida.append (lista.pop(i))  #acá está el error porque remueve el item iterado de la lista y la va vaciando
#     return invertida

# l = [1, 2, 3, 4, 5]
# m = invertir_lista(l)
# print(f'Entrada {l}, Salida: {m}')

# debbuggeado
#%%
def invertir_lista(lista):
    """Recibe una lista L y la develve invertida."""
    invertida = []
    i = len(lista)
    while i > 0:  # tomo el último elemento
        invertida.append(
            i
        )  # acá está el error porque remueve el item iterado de la lista y la va vaciando
        i = i - 1
    return invertida


l = [1, 2, 3, 4, 5]
m = invertir_lista(l)
print(f"Entrada {l}, Salida: {m}")
