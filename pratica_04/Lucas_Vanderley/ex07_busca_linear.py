estudantes = ["Ana", "Bruno", "Carla", "Daniel"]
procurado = "Carla"

encontrado = False
for estudar in estudantes:
    if estudantes == procurado:
        encontrado = True


        break  
        
if encontrado:
    print(f"O estudante '{procurado}' foi encontrado na lista!")
else:
    print(f"O estudante '{procurado}' NÃO foi encontrado na lista.")
