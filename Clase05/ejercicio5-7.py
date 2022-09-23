import numpy as np

v1 = np.arange(1, 20, 2)
v2 = np.linspace(1, 19, 10)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x, y), axis=0)

"""
ndarray.ndim => te dice la cantidad de ejes (o dimensiones) del arreglo.

ndarray.shape => te va a dar una tupla de enteros que indican la cantidad de elementos en cada eje. 
Si tenés una matriz con 2 filas y 3 columnas de va a dar (2, 3).

ndarray.size => te dice la cantidad de elementos (cantidad de números) de tu arreglo. Es el producto 
de la tupla shape. En el ejemplo del renglón anterior, el size es 6.
"""

array_ejemplo = np.array(
    [
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
        [[0, 1, 2, 3], [4, 5, 6, 7]],
    ]
)
array_ejemplo.ndim  # cantidad de dimensiones # 3
array_ejemplo.shape  # cantidad de elementos en cada eje # (3, 2, 4)
array_ejemplo.size  # total de elementos 3*2*4 #24


a = np.arange(6)
b = a.reshape(3, 2)

a = np.array([1, 2, 3, 4, 5, 6])
a.shape
vec_fila = a[np.newaxis, :]
vec_fila.shape

vec_col = a[:, np.newaxis]
vec_col.shape

data = np.array([1, 2, 3])
data[1]
data[0:2]
data[1:]
data[-2:]

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])

five_up = a >= 5
print(a[five_up])

pares = a[a % 2 == 0]
print(pares)

c = a[(a > 2) & (a < 11)]
print(c)

five_up = (a > 5) | (a == 5)
print(five_up)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
print(b)

lista_de_coordenadas = list(zip(b[0], b[1]))

for coord in lista_de_coordenadas:
    print(coord)
    (0, 0)
    (0, 1)
    (0, 2)
    (0, 3)

print(a[b])

no_hay = np.nonzero(a == 42)
print(no_hay)

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
data + ones

a = np.array([1, 2, 3, 4])
a.sum()

b = np.array([[1, 1], [2, 2]])
b.sum(axis=0)
b.sum(axis=1)

data = np.array([1.0, 2.0])
data * 1.6

a = np.array([1, 2, 3, 4, 5, 6])
np.save("filename", a)
b = np.load("filename.npy")
print(b)
csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt("new_file.csv", csv_arr)
np.loadtxt("new_file.csv")
