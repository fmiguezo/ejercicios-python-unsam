# Ejercicio 10.9: Un pipeline más en serio

from vigilante import vigilar
import csv

lines = vigilar("../Data/mercadolog.csv")
rows = csv.reader(lines)
for row in rows:
    print(row)
