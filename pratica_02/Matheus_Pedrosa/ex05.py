contagem_positivos = 0
for i in range(10):
    valor = float(input(f'Digite o número {i + 1}: '))
    if valor > 0:
        contagem_positivos += 1
print(f'Foram digitados {contagem_positivos} números positivos.')
