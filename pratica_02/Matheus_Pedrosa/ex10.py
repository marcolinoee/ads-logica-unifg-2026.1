while True:
    print('1 - Somar')
    print('2 - Subtrair')
    print('0 - Sair')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        print(f'Resultado: {a + b}')
    elif opcao == '2':
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        print(f'Resultado: {a - b}')
    elif opcao == '0':
        print('Encerrando o programa.')
        break
    else:
        print('Opção inválida.')