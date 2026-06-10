# ex10.py
opcao = -1
while opcao != 0:
    print("\n1 - Somar\n2 - Subtrair\n0 - Sair")
    opcao = int(input("Escolha: "))
    if opcao == 1:
        a = float(input("Numero 1: "))
        b = float(input("Numero 2: "))
        print(f"Resultado: {a + b}")
    elif opcao == 2:
        a = float(input("Numero 1: "))
        b = float(input("Numero 2: "))
        print(f"Resultado: {a - b}")
    elif opcao == 0:
        print("Encerrando...")
    else:
        print("Opcao invalida.")
