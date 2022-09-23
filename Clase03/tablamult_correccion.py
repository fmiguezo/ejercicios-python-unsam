#%% con producto
def tabla():
    for x in range(5):
        for y in range(5):
            print(x * y)


#%% con suma
def tabla(N):
    print("      ", end="")
    for j in range(N):
        print(f"{j:>5}", end="")

    for x in range(N):
        valor = 0
        print()

        print(f"{x:>5}|", end="")
        for y in range(N):
            print(f"{valor:>5}", end="")
            valor = valor + x


tabla(10)
