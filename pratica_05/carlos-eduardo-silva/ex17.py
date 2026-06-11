notas = [[8.0,7.5,9.0],[5.0,6.0,5.5],[9.0,8.5,10.0],[6.5,7.0,6.0]]
menor_media = None
av_menor = 0
for j in range(len(notas[0])):
    soma = sum(notas[i][j] for i in range(len(notas)))
    media = soma / len(notas)
    if menor_media is None or media < menor_media:
        menor_media = media
        av_menor = j
print(f"Avaliação com menor média: {av_menor}")
print(f"Média: {menor_media:.2f}")
