# Ejercicio 10.13: Expresiones generadoras

nums = [1, 2, 3, 4, 5]
cuadrados = (x * x for x in nums)
for n in cuadrados:
    print(n)
