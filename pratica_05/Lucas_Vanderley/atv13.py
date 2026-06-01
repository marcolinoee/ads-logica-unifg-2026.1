nomes = ["Ana", "Bruno", "Carla", "Diego"]
notas = [
    [8.0, 7.5, 9.0],
    [5.0, 6.0, 5.5],
    [9.0, 8.5, 10.0],
    [6.5, 7.0, 6.0]
]

for nome, notas_aluno in zip(nomes, notas):
   
    media = sum(notas_aluno) / len(notas_aluno)
    
    print(f"{nome} - Média: {media:.2f}")