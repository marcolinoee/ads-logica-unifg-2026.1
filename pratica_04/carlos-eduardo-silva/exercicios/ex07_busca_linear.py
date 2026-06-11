# Exercício 7 - Busca linear de um elemento
estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"
encontrado = False
for estudante in estudantes:
    if estudante == procurado:
        encontrado = True
        break
if encontrado:
    print(f"{procurado} está na lista.")
else:
    print(f"{procurado} não está na lista.")
