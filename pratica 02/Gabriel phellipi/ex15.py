maior = 0
for i in range(1,6):
    notaAtual = (float(input(f"Digite a nota do {i}º aluno: ")))
    if notaAtual > maior:
        maior = notaAtual
print(f"{maior} essa é a maior nota")
