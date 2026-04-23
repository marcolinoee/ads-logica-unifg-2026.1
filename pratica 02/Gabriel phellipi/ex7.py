contar_pares = 0
for i in range(1,9):
    numero = (int(input("Digite um numero: ")))
    if numero % 2 == 0:
        contar_pares += 1
print(f"tem {contar_pares} numeros pares.")        