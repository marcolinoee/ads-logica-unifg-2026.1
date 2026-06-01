nomes = ["Ana", "Bruno", "Carla", "Diego"]
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

medias = [sum(aluno) / len(aluno) for aluno in notas]


maior_media = max(medias)


indice_maior = medias.index(maior_media)
melhor_aluno = nomes[indice_maior]

print(f"Maior média: {melhor_aluno} - {maior_media:.2f}")