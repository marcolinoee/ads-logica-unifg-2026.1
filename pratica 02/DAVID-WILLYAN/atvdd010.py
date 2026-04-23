opcao = -1

while opcao != 0:
    print("\n--- MENU ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 + n2)
        
    elif opcao == 2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("Resultado:", n1 - n2)
        
    elif opcao == 0:
        print("Saindo do programa...")
        
    else:
        print("Opção inválida! Tente novamente.")