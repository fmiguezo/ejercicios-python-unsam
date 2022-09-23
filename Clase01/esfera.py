# esfera.py
# Ejercicio 1.13: El volumen de una esfera

from math import pi

radio = float(input("Ingrese el radio de la esfera en centímetros:\n"))
volumen = 4 / 3 * pi * radio ** 3
print("El volumen de la esfera es", volumen, " cm³")
