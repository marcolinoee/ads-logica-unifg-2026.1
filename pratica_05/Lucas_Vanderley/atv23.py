presencas = [
    ["P", "P", "F", "P", "P"],
    ["P", "F", "F", "P", "P"],
    ["P", "P", "P", "P", "F"],
    ["F", "P", "P", "F", "P"]
]

faltas_por_aula = [coluna.count("F") for coluna in zip(*presencas)]

maior_falta = max(faltas_por_aula)
aula_pior = faltas_por_aula.index(maior_falta)

print(f"A aula com mais faltas foi a Aula {aula_pior} (Total: {maior_falta} faltas)")