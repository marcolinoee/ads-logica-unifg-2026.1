total = 0

continuar = "S"

while continuar == "S":
    valor = float(input("Valor da compra: "))
    total += valor

    continuar = input("Deseja continuar? (S/N): ").upper()

print(f"Total gasto: R$ {total:.2f}")