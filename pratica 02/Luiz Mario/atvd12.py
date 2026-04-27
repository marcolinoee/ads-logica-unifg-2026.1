total = 0
quantidade = 0
continuar = "S"

while continuar.upper() == "S":
    valor = float(input("Digite o valor da compra: R$ "))
    total += valor
    quantidade += 1

    continuar = input("Deseja continuar? (S/N): ")

print(f"\n===== RESUMO DAS COMPRAS =====")
print(f"Compras realizadas:  {quantidade}")
print(f"Total gasto:         R$ {total:.2f}")
print(f"Média por compra:    R$ {total / quantidade:.2f}")