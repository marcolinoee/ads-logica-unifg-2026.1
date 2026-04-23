for tentativa in range(10000):
    senha = (input("Digite a senha: "))
    if senha == "acesso":
        print("Acesso permitido")
        break
    else:
        print("Acesso negado")    