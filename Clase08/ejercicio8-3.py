# Ejercicio 8.3: Fecha de reincorporación
from datetime import date, timedelta

comienzo = date(2020, 9, 26)
licencia = timedelta(days=200)

reincorporacion = comienzo + licencia
