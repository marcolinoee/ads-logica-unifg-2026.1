# Exercício 1 - Limpeza e padronização de nomes
nomes_brutos = ["  ana", "BRUNO  ", "cArLa silva", "  joão pedro  "]
nomes_padronizados = []
for nome in nomes_brutos:
    nomes_padronizados.append(nome.strip().title())
print(nomes_padronizados)
print(f"Total de nomes: {len(nomes_padronizados)}")
