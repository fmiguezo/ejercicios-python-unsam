# Ejercicio 6.2: Propagar por como el auto fantástico


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

"""
Preguntas: 
    1. ¿Por qué se modificó la lista original? 
    2. ¿Por qué no quedó igual al estado propagado? 
    3. Corregí el código para que no cambie la lista de entrada. 
    4. ¿Cuántas operaciones hace como máximo propagar_a_derecha en una lista de 
    largo n? 
    5. Sabiendo que invertir una lista ([::-1]) requiere una cantidad lineal de 
    operaciones en la longitud de la lista ¿Cuántas operaciones hace como máximo 
    propagar en una lista de largo n?
"""
