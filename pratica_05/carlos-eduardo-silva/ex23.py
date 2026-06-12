presencas = [["P","P","F","P","P"],["P","F","F","P","P"],["P","P","P","P","F"],["F","P","P","F","P"]]
mais_faltas = 0
aula_mais = 0
for j in range(len(presencas[0])):
    faltas = sum(1 for i in range(len(presencas)) if presencas[i][j] == "F")
    if faltas > mais_faltas:
        mais_faltas = faltas
        aula_mais = j
print(f"Aula com mais faltas: {aula_mais}")
print(f"Total de faltas: {mais_faltas}")
