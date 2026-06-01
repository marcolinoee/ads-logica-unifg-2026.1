presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]


todas_presencas = [status for linha in presencas for status in linha]

total_p = todas_presencas.count("P")
total_f = todas_presencas.count("F")

print(f"Total de presenças: {total_p}\nTotal de faltas: {total_f}")