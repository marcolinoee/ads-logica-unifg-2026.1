compras = []
while True:
    regitro = str(input("Digite sua compra: "))
    compras.append(regitro)
    continuar = str(input("Digite se você quiser contunuar Y/N")).upper()

    if continuar == "N":
        break
    elif continuar == "Y":
        print(f"Continue, por enquanto suas compras são {compras}")
    else:
        print("Error!")


print(f"Suas compras foram: {compras}")
