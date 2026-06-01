presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

for i, linha in enumerate(presencas):
    faltas = linha.count("F")
    print(f"Estudante {i} - Faltas: {faltas}")