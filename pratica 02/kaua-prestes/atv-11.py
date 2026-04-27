alunos_aprovados = 0
recuperacao = 0
alunos_reprovados = 0

alunos = int(input("Digite o número de alunos: "))

for i in range(alunos):
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 7:
        alunos_aprovados += 1
    elif nota >= 5 and nota < 7:
        recuperacao += 1
    else:
        alunos_reprovados += 1

print(f"Alunos aprovados: {alunos_aprovados}")
print(f"Alunos em recuperação: {recuperacao}")
print(f"Alunos reprovados: {alunos_reprovados}")