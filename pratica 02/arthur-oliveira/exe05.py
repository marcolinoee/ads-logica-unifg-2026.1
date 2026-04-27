contador_positivos = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero > 0:
        contador_positivos += 1

print(f"Quantidade de números positivos: {contador_positivos}")