while True:
    print("Escolha uma opção:\n1 - Somar\n2 - Subtrair\n0 - Sair")
    opcao = int(input())

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")

    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}\n")

    elif opcao == 0:
        break

    else:
        print("Opção inválida.\n")