estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

encontrado = False

for estudante in estudantes:
    if estudante == procurado:
        encontrado = True
        break

if encontrado:
    print(f'"{procurado}" foi encontrado na lista.')
else:
    print(f'"{procurado}" NÃO foi encontrado na lista.')

procurado2 = "Fernanda"
encontrado2 = False

for estudante in estudantes:
    if estudante == procurado2:
        encontrado2 = True
        break

if encontrado2:
    print(f'"{procurado2}" foi encontrado na lista.')
else:
    print(f'"{procurado2}" NÃO foi encontrado na lista.')
