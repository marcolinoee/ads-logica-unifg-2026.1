Numbers = int(input("Digite 1-Somar , 2-Subtrair , 0-Sair "))
Number1 = int(input("Digite 1 Numero "))
Number2 = int(input("Digite Outro Numero "))
add = 1
subtract = 2
for i in range (1,5):
    if Numbers==add:
        print(Number1+Number2)
    elif Numbers==subtract:
        print(Number1-Number2)
    else:
        print("Opção invalida")
    Numbers = int(input("Digite 1-Somar , 2-Subtrair , 0-Sair "))
    Number1 = int(input("Digite 1 Numero "))
    Number2 = int(input("Digite Outro Numero "))
