# arbolado_parques_veredas.py
# Ejercicio 8.9: Comparando especies en parques y en veredas

import pandas as pd
import os
import sys


def df(directorio, archivo, cols_sel, especies, ambiente):
    fname = os.path.join(directorio, archivo)
    df = pd.read_csv(fname)
    df_lineal = df[cols_sel]
    df_especie = df_lineal[df_lineal.iloc[:, 0].isin(especies)].copy()
    df_especie.rename(
        columns={
            df_especie.columns[0]: "Nombre científico",
            df_especie.columns[1]: "Diámetro",
            df_especie.columns[2]: "Altura total",
        },
        inplace=True,
    )
    df_especie.insert(3, "Ambiente", ambiente, allow_duplicates=True)
    return df_especie


def f_principal(argv):
    directorio = "../Data"
    archivo_veredas = "arbolado-publico-lineal-2017-2018.csv"
    archivo_parques = "arbolado-en-espacios-verdes.csv"
    cols_sel_veredas = ["nombre_cientifico", "diametro_altura_pecho", "altura_arbol"]
    especies_seleccionadas_veredas = ["Tipuana tipu"]
    cols_sel_parques = ["nombre_cie", "diametro", "altura_tot"]
    especies_seleccionadas_parques = ["Tipuana Tipu"]

    df_tipas_veredas = df(
        directorio,
        archivo_veredas,
        cols_sel_veredas,
        especies_seleccionadas_veredas,
        "Veredas",
    )
    df_tipas_parques = df(
        directorio,
        archivo_parques,
        cols_sel_parques,
        especies_seleccionadas_parques,
        "Parques",
    )

    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

    df_tipas.boxplot("Diámetro", by="Ambiente")
    df_tipas.boxplot("Altura total", by="Ambiente")


if __name__ == "__main__":
    f_principal(sys.argv)
