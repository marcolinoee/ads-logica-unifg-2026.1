
estudantes_bruto = ["  lucas ", "AMANDA", "caio mello", "Beatriz  ", "  lucas"]
notas = [4.5, 8.5, 7.0, 5.5, 9.2]
consulta = "amanda"


estudantes_limpos = []
for nome in estudantes_bruto:
    estudantes_limpos.append(nome.strip().lower())

consulta_padronizada = consulta.strip().lower()



notas_aprovadas = []
for nota in notas:
    if nota >= 7.0:
        notas_aprovadas.append(nota)



esta_presente = False
for aluno in estudantes_limpos:
    if aluno == consulta_padronizada:
        esta_presente = True
        break



print("=" * 15, "RELATÓRIO FINAL", "=" * 15)
print(f"Estudantes cadastrados (Padronizados): {estudantes_limpos}")
print(f"Notas consideradas aprovadas (>= 7.0): {notas_aprovadas}")
print("-" * 47)

if esta_presente:
    print(f"Resultado da Consulta: '{consulta.title()}' está PRESENTE.")
else:
    print(f"Resultado da Consulta: '{consulta.title()}' está AUSENTE.")
print("=" * 47)