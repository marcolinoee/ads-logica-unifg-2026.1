presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

presentes = []

for nome in presentes_bruto:
    presentes.append(nome.strip().title())

consulta_padronizada = consulta.strip().title()

encontrado = False

for nome in presentes:
    if nome == consulta_padronizada:
        encontrado = True
        break

print(presentes)

if encontrado:
    print("Presente")
else:
    print("Ausente")