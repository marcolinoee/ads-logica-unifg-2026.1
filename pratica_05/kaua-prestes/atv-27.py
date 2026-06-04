print("Resultado exibido: [[1, 0, 0], [1, 0, 0], [1, 0, 0]]")
print("Isso ocorre porque [[0]*3]*3 cria três referências para a mesma lista.")
print("Alterar uma linha altera todas as outras simultaneamente.")
print()

matriz = [[0] * 3 for _ in range(3)]
matriz[0][0] = 1
print(matriz)
