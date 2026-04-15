    # Exercicio 10

somar = 1
subtrair = 2

for i in range (5):
    numero_1 = float(input("Digite um numero:"))
    numero_2 = float(input("Digite outro numero:"))
    calculo = int(input("Digite 1-somar 2-subtrai:"))

    if (calculo == somar):
        print(numero_1 + numero_2)
    elif (calculo == subtrair):
        print(numero_1 - numero_2)
    else:
        print("Opção invalido!")

    # O codigo ficou mais simples ja que tirou algumas linhas e usar ficou mais facil