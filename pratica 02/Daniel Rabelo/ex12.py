total_compras = 0
continuar = "S"

while continuar.upper() == "S":
    valor = float(input("Digite o valor da compra: R$ "))
    total_compras += valor
    continuar = input("Deseja continuar? (S/N): ")

print("-" * 30)
print(f"Programa encerrado.")
print(f"O valor total de todas as compras foi: R$ {total_compras:.2f}")