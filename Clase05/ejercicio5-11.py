## Ejercicio 5.11: Incompleto
import random
import numpy as np


def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    return album


figus_total = 670


def album_incompleto(A):
    A.sort()
    if A[0] == 0:
        return True
    else:
        return False
