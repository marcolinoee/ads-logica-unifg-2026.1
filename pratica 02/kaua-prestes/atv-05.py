contador_positivos = 0

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    if num > 0:
        contador_positivos += 1

print(f"números positivos: {contador_positivos}")