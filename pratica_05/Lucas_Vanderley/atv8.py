matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matriz)):
    
    for j in range(len(matriz[i])):
        
        valor = matriz[i][j]

        print(f"Linha {i} Coluna {j} Valor {valor}")