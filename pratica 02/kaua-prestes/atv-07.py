soma = 0
print("Digite 8 números inteiros:")

for i in range(8):
    num = int(input())
    if num % 2 == 0:
        soma += num
print(f"A soma dos números pares é: {soma}")