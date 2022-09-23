# Ejercicio 4.6: Propagación
#%%
def propagar(lista):
    for i, f in enumerate(lista):  # recorro la lista
        if (f == 1) and (i < len(lista) - 1) and (lista[i + 1] == 0):
            lista[i + 1] = 1
        for i in range(len(lista)):
            if (lista[i] == 1) and (lista[i - 1] == 0):
                lista[i - 1] = 1
                i -= 1
    return lista


propagar(
    [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
)  # [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
propagar([0, 0, 0, 1, 0, 0])  # [1, 1, 1, 1, 1, 1]


# #%%
# def propagar1(l):
#     L=len(l)
#     cambio = True
#     while cambio:
#         cambio = False
#         for i,e in enumerate(l):
#             if e == 1:
#                 if l>0 and l[i-1]==0:
#                     cambio = True
#                     l[i-1]=1
#                 if i<L-1 and l[i+1]==0:
#                     cambio = True
#                     l[i+1]=1

# l = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
# propagar1(l)

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
