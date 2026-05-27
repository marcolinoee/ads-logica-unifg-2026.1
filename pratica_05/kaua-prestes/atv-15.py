nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

maior_media = -1
melhor_aluno = ""

for i in range(len(nomes)):
    soma = 0
    for nota in notas[i]:
        soma += nota
    media = soma / len(notas[i])
    if media > maior_media:
        maior_media = media
        melhor_aluno = nomes[i]

print(f"Maior média: {melhor_aluno} - {maior_media:.2f}")
