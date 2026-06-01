nomes = ["Ana", "Bruno", "Carla", "Diego", "Elena"]
notas = [
    [8.0, 7.5, 9.0, 8.5],
    [5.0, 6.0, 5.5, 6.5],
    [9.0, 8.5, 10.0, 9.5],
    [4.0, 3.5, 5.0, 4.5],
    [7.0, 6.5, 7.5, 8.0]
]

medias = []

for nome, notas_aluno in zip(nomes, notas):
    media = sum(notas_aluno) / len(notas_aluno)
    medias.append(media)
    
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
        
    print(f"{nome} - Média: {media:.2f} - Situação: {situacao}")

print("-" * 30)


maior_media = max(medias)
menor_media = min(medias)

print(f"Maior média da turma: {nomes[medias.index(maior_media)]} ({maior_media:.2f})")
print(f"Menor média da turma: {nomes[medias.index(menor_media)]} ({menor_media:.2f})")