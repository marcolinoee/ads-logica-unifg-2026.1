presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

num_aulas = len(presencas[0])
mais_faltas = -1
aula_mais_faltas = -1

for j in range(num_aulas):
    faltas = 0
    for i in range(len(presencas)):
        if presencas[i][j] == "F":
            faltas += 1
    if faltas > mais_faltas:
        mais_faltas = faltas
        aula_mais_faltas = j

print(f"Aula com mais faltas: {aula_mais_faltas}")
print(f"Total de faltas: {mais_faltas}")
