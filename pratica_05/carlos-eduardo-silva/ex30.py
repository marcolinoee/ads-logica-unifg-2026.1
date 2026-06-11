lab = [["L","O","L","M","L"],["O","L","L","O","M"],["L","M","O","L","L"],["O","L","M","L","O"]]
for linha in lab:
    print(linha)
livres = sum(l.count("L") for l in lab)
ocupados = sum(l.count("O") for l in lab)
manutencao = sum(l.count("M") for l in lab)
print(f"Livres: {livres} | Ocupados: {ocupados} | Manutenção: {manutencao}")
li, co = 0, 2
if li >= len(lab) or co >= len(lab[0]):
    print("Fora dos limites!")
elif lab[li][co] == "L":
    lab[li][co] = "O"
    print("Ocupado com sucesso!")
elif lab[li][co] == "M":
    print("Em manutenção!")
else:
    print("Já ocupado!")
for linha in lab:
    print(linha)
