# Ejercicio 4.5: Invertir una lista
#%%
def invertir_lista(lista):
    invertida = []
    i = len(lista)
    for e in lista:  # Recorro la lista
        invertida.append(
            lista[i - 1]
        )  # agrego los elementos de atrás para adelante, empezando en la posición -1 de la lista
        i = i - 1  # agrego el elemento e al principio de la lista invertida
    return invertida


l1 = [1, 2, 3, 4, 5]
l2 = ["Bogotá", "Rosario", "Santiago", "San Fernando", "San Miguel"]
invertir_lista(l1)
invertir_lista(l2)
