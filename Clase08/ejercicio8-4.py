# Ejercicio 8.4: Días hábiles

from datetime import datetime, timedelta
import sys


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def dias_habiles(inicio, fin, feriados):
    inicio_conv = datetime.strptime(inicio, "%d/%m/%Y")
    fin_conv = datetime.strptime(fin, "%d/%m/%Y")
    feriados_conv = []
    for i in range(len(feriados)):
        feriados_conv.append(datetime.strptime(feriados[i], "%d/%m/%Y"))
    contador = 0
    for dia in daterange(inicio_conv, fin_conv):
        if dia not in feriados_conv:
            if dia.weekday() != 5 and dia.weekday() != 6:
                contador += 1
    return contador


def f_principal(argv):
    inicio = "20/09/2020"
    fin = "31/12/2020"
    feriados = ["12/10/2020", "23/11/2020", "7/12/2020", "8/12/2020", "25/12/2020"]
    dias_habiles(inicio, fin, feriados)


if __name__ == "__main__":
    f_principal(sys.argv)
