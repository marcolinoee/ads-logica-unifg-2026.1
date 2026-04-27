quantidade = int(input("Digite a quantidade de alunos: "))

aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(1, quantidade + 1):
    media = float(input(f"Digite a média do aluno {i}: "))

    if media >= 7:
        aprovados += 1
    elif media >= 4:
        recuperacao += 1
    else:
        reprovados += 1

print(f"\n===== RESULTADO FINAL =====")
print(f"Aprovados:    {aprovados}")
print(f"Recuperação:  {recuperacao}")
print(f"Reprovados:   {reprovados}")