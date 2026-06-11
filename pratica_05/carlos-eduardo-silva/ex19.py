sala = [["L","O","L"],["O","O","L"],["L","L","O"]]
livres = 0
ocupados = 0
for linha in sala:
    for a in linha:
        if a == "L":
            livres += 1
        else:
            ocupados += 1
print("Assentos livres:", livres)
print("Assentos ocupados:", ocupados)
