notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

medias_avaliacoes = [sum(coluna) / len(coluna) for coluna in zip(*notas)]

menor_media = min(medias_avaliacoes)
indice_menor = medias_avaliacoes.index(menor_media)

print(f"Avaliação com menor média: {indice_menor}\nMédia: {menor_media:.2f}")