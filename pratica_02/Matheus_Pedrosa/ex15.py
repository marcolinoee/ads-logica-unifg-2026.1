maior_nota = None
for i in range(5):
    nota = float(input(f'Digite a nota {i + 1}: '))
    if maior_nota is None or nota > maior_nota:
        maior_nota = nota
print(f'A maior nota é: {maior_nota:.2f}')