notas = [[8,7,9],[5,6,5],[9,10,8]]
for i in range(len(notas)):
    soma = 0
    for j in range(len(notas[i])):
        soma += notas[i][j]
    print(f"Média estudante {i}: {soma/len(notas[i]):.2f}")
