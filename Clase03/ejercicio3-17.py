print(" " * 4, end="")
for e in range(0, 10):
    print(f"{e:^4d}", end="")
print("")
print("-" * (43))

for i in range(0, 10):
    print(f"{i}:", end="")
    for j in range(0, 10):
        print(f"{i*j:>4d}", end="")
    print("")
