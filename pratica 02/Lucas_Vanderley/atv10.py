while True:
    valor = int(input("Digite seu valor: "))
    valor1 = int(input("Digite seu valor: "))
    soma = valor + valor1
    subtracao = valor - valor1
    opcao = int(input("Digite uma opção entre 1 ou 2: "))
    

    if opcao == 1:
        print(f"{valor} + {valor1} = {soma}")
    elif opcao == 2:
        print(f"{valor} - {valor1} = {subtracao}")
    elif opcao == 0:
        break
    else:
        print("Digite uma opção valida!")


