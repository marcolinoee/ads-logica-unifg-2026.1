quantidade = int(input('Digite a quantidade de alunos: '))
aprovados = 0
recuperacao = 0
reprovados = 0
for i in range(quantidade):
    media = float(input(f'Digite a média do aluno {i + 1}: '))
    if media >= 7:
        aprovados += 1
    elif media >= 4:
        recuperacao += 1
    else:
        reprovados += 1
print(f'Aprovados: {aprovados}')
print(f'Recuperação: {recuperacao}')
print(f'Reprovados: {reprovados}')
