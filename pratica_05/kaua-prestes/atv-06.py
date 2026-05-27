dados = [
    [1, 2],
    [3, 4]
]

print("O código print(dados[2][0]) NÃO executa corretamente.")
print("Causa um IndexError pois a matriz possui apenas linhas de índice 0 e 1.")
print("Índices válidos para linhas: 0 e 1")
print()
print("Código corrigido para exibir o valor 3:")
print(dados[1][0])
