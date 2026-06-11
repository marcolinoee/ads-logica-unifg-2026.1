vendas = [[20,25,18,30],[15,22,20,19],[30,28,35,40]]
produtos = ["Produto 1","Produto 2","Produto 3"]
maior_p = None
prod_destaque = ""
for i in range(len(produtos)):
    total = sum(vendas[i])
    print(f"{produtos[i]} - Total: {total}")
    if maior_p is None or total > maior_p:
        maior_p = total
        prod_destaque = produtos[i]
maior_s = None
semana_destaque = 0
for j in range(len(vendas[0])):
    total = sum(vendas[i][j] for i in range(len(vendas)))
    print(f"Semana {j+1} - Total: {total}")
    if maior_s is None or total > maior_s:
        maior_s = total
        semana_destaque = j+1
print(f"\nMaior produto: {prod_destaque} - {maior_p}")
print(f"Maior semana: Semana {semana_destaque} - {maior_s}")
