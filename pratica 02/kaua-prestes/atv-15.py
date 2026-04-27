maior = 0

for i in range(5):
    notas = int(input("Digite 5 notas de alunos: "))
    if notas > maior:
        maior = notas

print(f"A maior nota é: {maior}")