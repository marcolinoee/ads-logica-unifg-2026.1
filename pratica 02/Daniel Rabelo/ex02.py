idade = -1
while idade != 0:
    idade = int(input("Digite a idade."))
    if idade < 18 and idade !=0:
        print("Classificação: You are Kid, grow up more!👦")
    elif 18 <= idade <= 59 and idade !=0:
        print("Classificação: O HOMI AGORA É ADULTO😎!")
    else:
        print("Classificação: Você é aposentado, meus parabéns IDOSO!👨‍🦳")
