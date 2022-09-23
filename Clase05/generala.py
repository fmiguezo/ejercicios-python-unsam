## Ejercicio 5.2: Generala no necesariamente servida

import random

#%%
def tirar(cubilete):
    tirada = [random.randint(1, 6) for _ in range(cubilete)]
    # tiro 5 números random entre 1 y 6 y armo una lista
    return tirada


#%%
def es_generala(tirada):
    return all(dado == tirada[0] for dado in tirada)  # comparo los 5 dados


#%%
def prob_generala(N):
    tiradas = 3
    dados = []
    for i in range(tiradas):
        dados = dados + tirar(5 - len(dados))
        if i < tiradas - 1:
            (cant, valor) = sorted(
                [(dados.count(dado), dado) for dado in range(1, 7)], reverse=True
            )[0]
            dados = [valor] * cant
    return es_generala(dados)


N = 1000000
G = sum([prob_generala(tirar(5)) for i in range(N)])
prob = G / N
print(f"Tiré {N} veces, de las cuales {G} saqué generala servida.")
print(f"Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.")
