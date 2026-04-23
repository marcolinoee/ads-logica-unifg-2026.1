tabuada = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada do {tabuada}:")
for i in range(11):
    mult = tabuada * i
    print(f"{tabuada} x {i} = {mult}")