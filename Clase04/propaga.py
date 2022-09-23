# Ejercicio 4.6: Propagación
#%%
def propagar(lista):
    for i, f in enumerate(lista):  # recorro la lista
        if (f == 1) and (i < len(lista) - 1) and (lista[i + 1] == 0):
            lista[i + 1] = 1
        for i in range(len(lista)):  # recorro a la izquierda
            if (lista[i] == 1) and (lista[i - 1] == 0):
                lista[i - 1] = 1
                i -= 1
    return lista


propagar(
    [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
)  # [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
propagar([0, 0, 0, 1, 0, 0])  # [1, 1, 1, 1, 1, 1]


## solucion video
# def propagar(lis):

#     for i,f in enumerate(lis):
#         if i-1 >=0:
#             if f ==0 and lis[i-1]==1:
#                 lis[i] = 1
#     for i in range(len(lis-1),-1, -1):
#         if i+1 < len(lis):
#             if lis[i]==0 and lis[i+1]==1:
#                 lis[i] = 1
#     return lis
