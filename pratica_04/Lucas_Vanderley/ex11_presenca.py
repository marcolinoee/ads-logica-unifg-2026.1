presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

presentes_limpos = [nome.strip().lower() for nome in presentes_bruto]
consulta_padronizada = consulta.strip().lower()

print(f"Lista de presença padronizada: {presentes_limpos}")
print("-" * 45)

if consulta_padronizada in presentes_limpos:
    print(f"O(A) estudante '{consulta.title()}' está PRESENTE!")
else:
    print(f"O(A) estudante '{consulta.title()}' está AUSENTE!")