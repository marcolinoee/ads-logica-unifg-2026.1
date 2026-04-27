senha=""

while senha != "acesso":
    senha = input("Digite a senha: ")

    if senha == "acesso":
        print("Acesso concedido!")
    elif senha == "Acesso":
        print("Senha incorreta! Dica: O Caps Lock está ativado ou você usou inicial maiúscula.")
    else:
        print("Senha incorreta. Tente novamente.")