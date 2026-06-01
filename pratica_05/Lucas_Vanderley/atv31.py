vendas = [
    [20, 25, 18, 30], 
    [15, 22, 20, 19], 
    [30, 28, 35, 40]   
]

total_por_produto = [sum(produto) for produto in vendas]
maior_produto = total_por_produto.index(max(total_por_produto))


total_por_semana = [sum(semana) for semana in zip(*vendas)]
maior_semana = total_por_semana.index(max(total_por_semana))


for i, total in enumerate(total_por_produto):
    print(f"Produto {i} - Total vendido: {total}")

print()
for j, total in enumerate(total_por_semana):
    print(f"Semana {j} - Total vendido: {total}")

print(f"\nProduto com maior volume de vendas: Produto {maior_produto}")
print(f"Semana com maior volume de vendas: Semana {maior_semana}")