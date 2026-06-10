# ex12.py
# Sem desconto: abaixo de R$100 | Basico: R$100-299 (10%) | Especial: acima R$300 (20%)
continuar = "s"
while continuar.lower() == "s":
    valor = float(input("Valor da compra: R$ "))
    if valor < 100:
        print(f"Sem desconto. Total: R$ {valor:.2f}")
    elif valor < 300:
        print(f"Desconto basico 10%. Total: R$ {valor * 0.9:.2f}")
    else:
        print(f"Desconto especial 20%. Total: R$ {valor * 0.8:.2f}")
    continuar = input("Outra compra? (s/n): ")
