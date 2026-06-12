nomes = ["Ana","Bruno","Carla","Diego"]
notas = [[8.0,7.5,9.0],[5.0,6.0,5.5],[9.0,8.5,10.0],[6.5,7.0,6.0]]
maior_media = 0
melhor = ""
for i in range(len(nomes)):
    media = sum(notas[i]) / len(notas[i])
    if media > maior_media:
        maior_media = media
        melhor = nomes[i]
print(f"Maior média: {melhor} - {maior_media:.2f}")
