nomes = ["Ana","Bruno","Carla","Diego","Eduardo"]
notas = [[8.0,7.5,9.0,8.5],[5.0,6.0,5.5,4.0],[9.0,8.5,10.0,9.5],[6.5,7.0,6.0,5.5],[3.0,4.0,3.5,4.5]]
maior_media = None
menor_media = None
aluno_maior = ""
aluno_menor = ""
for i in range(len(nomes)):
    media = sum(notas[i]) / len(notas[i])
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    print(f"{nomes[i]} - Média: {media:.2f} - {situacao}")
    if maior_media is None or media > maior_media:
        maior_media = media
        aluno_maior = nomes[i]
    if menor_media is None or media < menor_media:
        menor_media = media
        aluno_menor = nomes[i]
print(f"\nMaior média: {aluno_maior} - {maior_media:.2f}")
print(f"Menor média: {aluno_menor} - {menor_media:.2f}")
