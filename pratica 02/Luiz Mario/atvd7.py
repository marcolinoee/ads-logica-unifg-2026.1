contador = 0

for i in range(1, 9):
    numero = int(input(f"Digite o {i}º número: "))
    if numero % 2 == 0:
        contador += contador + numero

print(f"\nSoma dos números pares: {contador}")