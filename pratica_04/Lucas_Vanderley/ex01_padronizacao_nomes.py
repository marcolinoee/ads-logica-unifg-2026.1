nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]

nomes_padronizados = []

for nomes in nomes_brutos:
    y = nomes.strip().title()
    nomes_padronizados.append(y)

print(nomes_padronizados)
