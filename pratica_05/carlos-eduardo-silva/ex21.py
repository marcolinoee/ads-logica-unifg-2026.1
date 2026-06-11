presencas = [["P","P","F","P","P"],["P","F","F","P","P"],["P","P","P","P","F"],["F","P","P","F","P"]]
total_p = 0
total_f = 0
for linha in presencas:
    for r in linha:
        if r == "P":
            total_p += 1
        else:
            total_f += 1
print("Total de presenças:", total_p)
print("Total de faltas:", total_f)
