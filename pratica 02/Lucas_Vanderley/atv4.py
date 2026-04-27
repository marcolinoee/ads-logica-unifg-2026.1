while True:
    comando = input("Digite a senha: ")

    if comando == 'Acesso':
        break
        
    if len(comando) < 3:
        print("Muito curto, tente novamente.")
        continue

    print(f"Senha errada!")