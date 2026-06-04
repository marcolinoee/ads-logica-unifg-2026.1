nomes = ["Ana", "Bruno", "Carla", "Diego", "Eduardo"]

notas = [
    [8.0, 7.5, 9.0, 6.5],
    [5.0, 6.0, 5.5, 4.0],
    [9.0, 8.5, 10.0, 9.5],
    [6.5, 7.0, 6.0, 5.5],
    [3.0, 4.0, 3.5, 4.5]
]

medias = []

for i in range(len(nomes)):
    soma = 0
    for nota in notas[i]:
        soma += nota
    media = soma / len(notas[i])
    medias.append(media)

    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"{nomes[i]} - Média: {media:.2f} - {situacao}")

maior_media = medias[0]
menor_media = medias[0]
nome_maior = nomes[0]
nome_menor = nomes[0]

for i in range(len(medias)):
    if medias[i] > maior_media:
        maior_media = medias[i]
        nome_maior = nomes[i]
    if medias[i] < menor_media:
        menor_media = medias[i]
        nome_menor = nomes[i]

print(f"\nMaior média: {nome_maior} - {maior_media:.2f}")
print(f"Menor média: {nome_menor} - {menor_media:.2f}")
