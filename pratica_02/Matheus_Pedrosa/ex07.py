soma_pares = 0
for i in range(8):
    valor = int(input(f'Digite o valor inteiro {i + 1}: '))

    if valor % 2 == 0:
        soma_pares += valor
print(f'Soma dos números pares: {soma_pares}')