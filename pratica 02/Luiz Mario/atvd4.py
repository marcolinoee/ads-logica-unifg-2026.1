senha = (input("Digite sua senha: "))
while senha != "acesso":
    senha = (input("Digite sua senha novamente: "))
while senha == "acesso":
    print ("Acesso autorizado!")
    break
    