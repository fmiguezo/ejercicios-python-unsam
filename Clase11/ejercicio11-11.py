# Ejercicio 11.11: Búsqueda binaria


def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista) // 2
        if lista[medio] == e:
            res = True
        else:
            if e < lista[medio]:
                return bbinaria_rec(lista[:medio], e)
            else:
                return bbinaria_rec(lista[medio + 1 :], e)
    return res
