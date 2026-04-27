calculo = int(input("Digite 1-somar 2-subtrair 0-sair:"))
numero_1 = float(input("Digite um numero:"))
numero_2 = float(input("Digite outro numero:"))

somar = 1
subtrair = 2
sair = 0

while (calculo != sair):
    if (calculo == somar):
        print(numero_1 + numero_2)
    elif (calculo == subtrair):
        print(numero_1 - numero_2)
    else:
        print("Opção invalido!")
    numero_1 = float(input("Digite um numero:"))
    numero_2 = float(input("Digite outro numero:"))
    calculo = int(input("Digite 1-somar 2-subtrair 0-sair:"))

