# Ejercicio 10.1: Iteradores, un ejemplo

a = [1, 9, 4, 25, 16]
i = a.__iter__()
i.__next__()


f = open("../Data/camion.csv")
f.__iter__()
next(f)
