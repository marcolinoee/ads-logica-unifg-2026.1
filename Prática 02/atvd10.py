opcao = -1

while opcao != 0:
    print("\n1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        a = float(input("Digite um número: "))
        b = float(input("Digite outro número: "))
        print(f"Resultado: {a + b}")

    elif opcao == 2:
        a = float(input("Digite um número: "))
        b = float(input("Digite outro número: "))
        print(f"Resultado: {a - b}")