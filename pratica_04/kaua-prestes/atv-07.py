estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

encontrado = False

for estudante in estudantes:
    if estudante == procurado:
        encontrado = True
        break

print(encontrado)