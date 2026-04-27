total = 0

while True: 
    compra = (float(input("Digite o valor da compra: ")))
    total += compra
    print(f"esse é o total das suas compras: {total}")
    opcao = (input("Deseja continuar (S/N): "))
    if opcao == 'N':
        break

print(f"total das compras: {total:.2f}")        