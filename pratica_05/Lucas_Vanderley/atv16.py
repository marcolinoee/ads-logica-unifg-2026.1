notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

for i, avaliacao in enumerate(zip(*notas)):
    media_turma = sum(avaliacao) / len(avaliacao)
    
    print(f"Avaliação {i} - Média: {media_turma:.2f}")