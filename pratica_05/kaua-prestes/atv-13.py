nomes = ["Ana", "Bruno", "Carla", "Diego"]

notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

for i in range(len(nomes)):
    soma = 0
    for nota in notas[i]:
        soma += nota
    media = soma / len(notas[i])
    print(f"{nomes[i]} - Média: {media:.2f}")
