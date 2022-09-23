# Ejercicio 4.14: Fijando ideas
import csv

f = open("../Data/dowstocks.csv")
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
record["date"] = tuple(map(int, record["date"].split("/")))
