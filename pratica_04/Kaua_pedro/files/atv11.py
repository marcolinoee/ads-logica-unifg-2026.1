presentes_bruto = ["  maria ", "JOÃO", "ana clara", "Bruno  ", "  carla"]
consulta = "joão"

presentes = []
for nome in presentes_bruto:
    presentes.append(nome.strip().title())

consulta_padronizada = consulta.strip().title()

print("Lista padronizada:", presentes)

encontrado = False
for nome in presentes:
    if nome == consulta_padronizada:
        encontrado = True
        break

if encontrado:
    print(f'"{consulta_padronizada}" está PRESENTE na lista.')
else:
    print(f'"{consulta_padronizada}" está AUSENTE na lista.')

consulta2 = "fernanda"
consulta2_padronizada = consulta2.strip().title()
encontrado2 = False

for nome in presentes:
    if nome == consulta2_padronizada:
        encontrado2 = True
        break

if encontrado2:
    print(f'"{consulta2_padronizada}" está PRESENTE na lista.')
else:
    print(f'"{consulta2_padronizada}" está AUSENTE na lista.')
