soma = 0

for i in range(8):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero % 2 == 0:
        soma += numero

print(f"Soma dos números pares: {soma}")