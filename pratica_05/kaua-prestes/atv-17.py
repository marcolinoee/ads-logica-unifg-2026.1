notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

num_avaliacoes = len(notas[0])
menor_media = float("inf")
avaliacao_menor = -1

for j in range(num_avaliacoes):
    soma = 0
    for i in range(len(notas)):
        soma += notas[i][j]
    media = soma / len(notas)
    if media < menor_media:
        menor_media = media
        avaliacao_menor = j

print(f"Avaliação com menor média: {avaliacao_menor}")
print(f"Média: {menor_media:.2f}")
