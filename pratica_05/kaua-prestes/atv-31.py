vendas = [
    [20, 25, 18, 30],
    [15, 22, 20, 19],
    [30, 28, 35, 40]
]

totais_produto = []
for i in range(len(vendas)):
    total = 0
    for v in vendas[i]:
        total += v
    totais_produto.append(total)
    print(f"Produto {i} - Total vendido: {total}")

print()

num_semanas = len(vendas[0])
totais_semana = []
for j in range(num_semanas):
    total = 0
    for i in range(len(vendas)):
        total += vendas[i][j]
    totais_semana.append(total)
    print(f"Semana {j} - Total vendido: {total}")

maior_total_produto = totais_produto[0]
indice_produto = 0
for i in range(len(totais_produto)):
    if totais_produto[i] > maior_total_produto:
        maior_total_produto = totais_produto[i]
        indice_produto = i

maior_total_semana = totais_semana[0]
indice_semana = 0
for j in range(len(totais_semana)):
    if totais_semana[j] > maior_total_semana:
        maior_total_semana = totais_semana[j]
        indice_semana = j

print(f"\nProduto com maior total: Produto {indice_produto} - {maior_total_produto}")
print(f"Semana com maior total: Semana {indice_semana} - {maior_total_semana}")
