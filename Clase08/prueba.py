# -*- coding: utf-8 -*-
import pandas as pd
import os

directorio = "../Data"
archivo = "arbolado-en-espacios-verdes.csv"
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)

df.head()
df.columns
df[["altura_tot", "diametro", "inclinacio"]].describe()
df["nombre_com"]
df["nombre_com"].unique()
df["nombre_com"] == "Ombú"
(df["nombre_com"] == "Ombú").sum()
cant_ejemplares = df["nombre_com"].value_counts()
cant_ejemplares.head(10)
df_jacarandas = df[df["nombre_com"] == "Jacarandá"]
cols = ["altura_tot", "diametro", "inclinacio"]
df_jacarandas = df_jacarandas[cols]
df_jacarandas.tail()
df_jacarandas.describe()
df_jacarandas = df[df["nombre_com"] == "Jacarandá"][cols].copy()
df_jacarandas.plot.scatter(x="diametro", y="altura_tot")

import seaborn as sns

sns.scatterplot(data=df_jacarandas, x="diametro", y="altura_tot")


cant_ejemplares.index
df.loc[165]
df_jacarandas.iloc[0]
cant_ejemplares.iloc[0:3]
df_jacarandas.iloc[-5:, 2]

df_jacarandas_diam = df_jacarandas["diametro"]
type(df_jacarandas)
type(df_jacarandas_diam)

pd.date_range("20200923", periods=7)
pd.date_range("20200923 14:00", periods=7)
pd.date_range("20200923 14:00", periods=7)
pd.date_range("20200923 14:00", periods=7)


import numpy as np

idx = pd.date_range("20200923 14:00", periods=120, freq="min")
s1 = pd.Series(np.random.randint(-1, 2, 120), index=idx)
s2 = s1.cumsum()

s2.plot()

w = 5  # ancho en minutos de la ventana
s3 = s2.rolling(w).mean()
s3.plot()

df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()
