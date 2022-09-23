# Ejercicio 6.10: Importar módulos

from fileparse import parse_csv

camion = parse_csv(
    "../Data/camion.csv",
    select=["nombre", "cajones", "precio"],
    types=[str, int, float],
)
