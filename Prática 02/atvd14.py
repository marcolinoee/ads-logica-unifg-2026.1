for tentativa in range(1000):  
    senha = input("Digite a senha: ")

    if senha == "vamoo":
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta, tente novamente.")