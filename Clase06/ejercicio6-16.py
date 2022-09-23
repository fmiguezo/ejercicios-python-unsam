# Ejercicio 6.16: Cálcular la complejidad de dos resoluciones de propagar
"""
Ahora que tenés algunas herramientas teóricas más, volvé a leer las dos versiones 
de propagar del Ejercicio 6.1 y el Ejercicio 6.2 y compará sus complejidades.
"""

#%% 6.1
def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i, e in enumerate(l):
        if e == 1 and i < n - 1 and l[i + 1] == 0:
            l[i + 1] = 1
            modif = True
        if e == 1 and i > 0 and l[i - 1] == 0:
            l[i - 1] = 1
            modif = True
    return modif


def propagar(l):
    m = l.copy()
    veces = 0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repet� {veces} veces la funci�n propagar_al_vecino.")
    print(f"Con input {m}")
    print(f"Y obtuve  {l}")
    return m


#%%
propagar([0, 0, 0, 0, 1])
propagar([0, 0, 1, 0, 0])
propagar([1, 0, 0, 0, 0])


#%% 6.2
def propagar_a_derecha(l):
    n = len(l)
    for i, e in enumerate(l):
        if e == 1 and i < n - 1:
            if l[i + 1] == 0:
                l[i + 1] = 1
    return l


#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]


#%
def propagar(l):
    ld = propagar_a_derecha(l)
    lp = propagar_a_izquierda(ld)
    return lp


#%%
l = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
print("Estado original:  ", l)
print("Porpagando...")
lp = propagar(l)
print("Estado original:  ", l)
print("Estado propagado: ", lp)
