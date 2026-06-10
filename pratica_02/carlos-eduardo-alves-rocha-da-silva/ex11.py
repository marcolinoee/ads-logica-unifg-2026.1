# ex11.py
qtd = int(input("Quantidade de alunos: "))
aprovados = recuperacao = reprovados = 0
for i in range(1, qtd + 1):
    media = float(input(f"Media do aluno {i}: "))
    if media >= 7:
        aprovados += 1
    elif media >= 4:
        recuperacao += 1
    else:
        reprovados += 1
print(f"Aprovados: {aprovados}")
print(f"Recuperacao: {recuperacao}")
print(f"Reprovados: {reprovados}")
