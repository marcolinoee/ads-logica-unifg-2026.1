# Exercício 11 - Cadastro simples de presença
presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"
presentes = []
for nome in presentes_bruto:
    presentes.append(nome.strip().title())
consulta_padronizada = consulta.strip().title()
print(presentes)
if consulta_padronizada in presentes:
    print(f"{consulta_padronizada} está presente.")
else:
    print(f"{consulta_padronizada} não está presente.")
