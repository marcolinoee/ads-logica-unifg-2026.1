total = 0
quantidade = 0
continuar = "S"

while continuar.upper() == "S":
    valor = float(input("Digite o valor da compra: R$ "))
    total += valor
    quantidade += 1
    continuar = input("Deseja continuar? (S/N): ")

print(f"Total gasto: R$ {total:.2f}")

# Foi mais simples sim!