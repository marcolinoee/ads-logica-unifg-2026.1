while True:
    print("=========== MENU INTERATIVO ============")
    print("1 - Somar")
    print("2 - subtrair")
    print("0 - sair")
    opcao = (int(input("Digite a opção: ")))
    if opcao == 1:
        numero = (float(input("Digite o primeiro numero para soma: ")))
        numero1 = (float(input("Digite outro numero: ")))
        print(numero + numero1)
    elif opcao == 2:
        numero = (float(input("Digite o primeiro numero para subtração: ")))
        numero1 = (float(input("Digite outro numero: ")))
        print(numero - numero1)
    elif opcao == 0:
        print("saindo do menu")
        break    


