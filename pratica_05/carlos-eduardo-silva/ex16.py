notas = [[8.0,7.5,9.0],[5.0,6.0,5.5],[9.0,8.5,10.0],[6.5,7.0,6.0]]
for j in range(len(notas[0])):
    soma = sum(notas[i][j] for i in range(len(notas)))
    print(f"Avaliação {j} - Média: {soma/len(notas):.2f}")
