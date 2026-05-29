nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]

nomes_padronizados = []

for nome in nomes_brutos:
    nomes_padronizados.append(nome.strip().title())

print("Nomes padronizados:", nomes_padronizados)

print("Quantidade de nomes:", len(nomes_padronizados))
