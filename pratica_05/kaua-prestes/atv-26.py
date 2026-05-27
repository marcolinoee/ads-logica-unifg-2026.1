dados = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

print("O erro ocorre pois dados[1] possui apenas 2 elementos.")
print("Ao tentar acessar dados[1][2], ocorre IndexError.")
print("Índices válidos para as linhas: 0, 1 e 2")
print()
print("Versão corrigida:")

for i in range(len(dados)):
    for j in range(len(dados[i])):
        print(dados[i][j])
