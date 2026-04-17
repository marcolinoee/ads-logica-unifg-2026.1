while True:
    print("\n--- MENU INTERATIVO ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da Soma: {n1 + n2} ")
        
    elif opcao =="2":
        n1 = float(input(f"Digite o primeiro número: "))
        n2 = float(input("Digite o segundo numero: "))
        print(f"Resultado da Subtração: {n1 - n2}")
        
    elif opcao == "0":
        print("Saindo do programa...Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")
