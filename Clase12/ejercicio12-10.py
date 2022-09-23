# Ejercicio 12.10: Seaborn

from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns

iris_dataset = load_iris()
# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset["data"], columns=iris_dataset.feature_names)
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie


# gráfico original con pandas
pd.plotting.scatter_matrix(
    iris_dataframe,
    c=iris_dataset["target"],
    figsize=(15, 15),
    marker="o",
    hist_kwds={"bins": 20},
    s=60,
    alpha=0.8,
)

# gráfico del ejercicio con seaborn
iris_dataframe["target"] = iris_dataset["target"]
s = sns.pairplot(
    iris_dataframe,
    hue="target",
    palette=["C4", "C2", "C8"],
    diag_kind="hist",
    diag_kws={"bins": 20, "alpha": 0.8},
)
s.fig.set_size_inches(15, 15)
