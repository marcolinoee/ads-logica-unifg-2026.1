qtd_alunos = int(input("Quantos alunos a turma possui? "))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(1,qtd_alunos + 1):
    media = float(input(f"Digite a média do {i}° aluno: "))

    if media >= 7:
        aprovados += 1
    elif media >= 4:
        recuperacao += 1
    else:
        reprovados += 1

print("-" * 30)
print("RELATÓRIO FINAL DA TURMA")        
print(f"Aprovados: {aprovados}")
print(f"Em Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")

