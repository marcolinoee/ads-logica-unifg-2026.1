opcao = -1

while opcao != 0:
    print("\n===== CALCULADORA =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        a = int(input("Digite o 1º número: "))
        b = int(input("Digite o 2º número: "))
        print(f"Resultado: {a} + {b} = {a + b}")

    elif opcao == 2:
        a = int(input("Digite o 1º número: "))
        b = int(input("Digite o 2º número: "))
        print(f"Resultado: {a} - {b} = {a - b}")

    elif opcao != 0:
        print("Opção inválida! Tente novamente.")

print("\nPrograma encerrado. Até logo!")