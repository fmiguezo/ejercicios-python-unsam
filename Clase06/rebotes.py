# rebotes.py
# Archivo de ejemplo
# Ejercicio 1.5: La pelota que rebota

altura = 100  # altura desde la que tiramos la pelota
rebotes = 0  # veces que rebota
distancia = 3 / 5  # distancia que recorre en cada rebote

while rebotes < 10:
    altura = altura * distancia
    rebotes = rebotes + 1
    print(rebotes, round(altura, 4))
