presencas = [["P","P","F","P","P"],["P","F","F","P","P"],["P","P","P","P","F"],["F","P","P","F","P"]]
for i in range(len(presencas)):
    faltas = presencas[i].count("F")
    print(f"Estudante {i} - Faltas: {faltas}")
