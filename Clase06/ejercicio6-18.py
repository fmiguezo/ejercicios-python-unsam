# Ejercicio 6.18: Un ejemplo más complejo


def incrementar(s):
    carry = 1
    l = len(s)

    for i in range(l - 1, -1, -1):
        if s[i] == 1 and carry == 1:
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


def listar_secuencias(n):
    s = [0] * n
    for i in range(n):
        incrementar(s)
        print(s)
    return
