import random
maior = 0
for x in range(6):
    nota = random.randint(0,10)
    aluno = random.randint(1,5)
    print(f"O aluno numero {aluno} ficou com a nota {nota}!")

    if nota > maior:
        maior = nota

print(f"A maior nota foi {maior}")
