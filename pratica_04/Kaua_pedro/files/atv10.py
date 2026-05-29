notas = [4.5, 7.0, 8.0, 5.5, 9.0, 6.8, 7.2]

aprovados = []

for nota in notas:
    if nota >= 7.0:
        aprovados.append(nota)

print("Notas aprovadas:", aprovados)

print(f"Quantidade de estudantes aprovados: {len(aprovados)}")
