# Ejercicio 7.11: Subplots fuera de una grilla

import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1)  # define la figura de arriba
plt.plot([0, 1, 2], [0, 1, 0])  # dibuja la curva
plt.xticks([]), plt.yticks([])  # saca las marcas

plt.subplot(
    2, 3, 4
)  # define la primera de abajo, que sería la cuarta si fuera una grilla regular de 3x3
plt.plot([0, 1], [0, 1])
plt.xticks([]), plt.yticks([])

plt.subplot(
    2, 3, 5
)  # define la segunda de abajo, que sería la quinta si fuera una grilla regular de 3x3
plt.plot([1, 0], [0, 0])
plt.xticks([]), plt.yticks([])

plt.subplot(
    2, 3, 6
)  # define la tercerra de abajo, que sería la sextaa figura si fuera una grilla regular de 3x3
plt.plot([0, 1], [1, 0])
plt.xticks([]), plt.yticks([])

plt.show()
