notas = [
    [8, 7, 9],
    [5, 6, 5],
    [9, 10, 8]
]

print("Problema: a variável soma não é reiniciada a cada nova linha,")
print("acumulando valores de todas as linhas anteriores e gerando médias incorretas.")
print()
print("Código corrigido:")

for i in range(len(notas)):
    soma = 0
    for j in range(len(notas[i])):
        soma += notas[i][j]
    media = soma / len(notas[i])
    print(media)
