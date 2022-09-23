# hojas_ISO.py
# Ejercicio 11.13: Hojas ISO y recursión

# solución recursiva
def medidas_hoja_A(N):
    """Calcula el tamaño de la hoja en formato ISO de A0 a A10"""
    base = (841, 1189)
    if N < 0 or N > 10:
        return "Formato inválido"
    if N == 0:
        return base
    if N > 0:
        val = medidas_hoja_A(N - 1)
        return (val[1] // 2, val[0])


# solución iterativa
# def medidas_hoja_A(N):
#     """Calcula el tamaño de la hoja en formato ISO de A0 a A10"""
#     if N < 0 or N > 10:
#        return
#     i = 0
#     base = (841, 1189)
#     for i in range(N):
#         base = (int(base[1] / 2), int(base[0]))
#     return base
