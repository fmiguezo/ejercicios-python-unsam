# Ejercicio 10.14: Expresiones generadoras como argumentos en funciones.
nums = [1, 2, 3, 4, 5]
sum([x * x for x in nums])  # una lista por comprensión
sum(x * x for x in nums)  # una expresión generadora
