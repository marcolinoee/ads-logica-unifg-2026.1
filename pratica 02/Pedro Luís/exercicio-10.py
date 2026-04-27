import os 
os.system("cls" if os.name == "nt" else "clear")
from time import sleep

def titulo(msg):
    tamanho = len(msg) + 4 
    print("-" * tamanho)
    print(msg.center(tamanho))
    print("-" * tamanho)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    titulo("MENU DE OPERAÇÕES")
    print("1 - Somar")
    print("2 - Subtrair")
    print("0 - Sair")
    while True:    
        escolha = input("Digite a sua opção: ").strip()
        if escolha not in "120" or escolha == "":
            print("DIGITE APENAS ENTRE AS OPÇÕES PRÉ-ESTABELECIDAS!")
            continue
        break
    if escolha == "1":
        while True:
            try:
                n1 = int(input("Digite o primeiro número: "))
            except ValueError:
                print("DIGITE APENAS NÚMEROS INTEIROS!")
                continue
            break
        while True:
            try:
                n2 = int(input("Digite o segundo número: "))
            except ValueError:
                print("DIGITE APENAS NÚMEROS INTEIROS!")
                continue
            break
        resultado = n1 + n2
        print(f"A soma entre {n1} e {n2} é igual a \033[32m{resultado}\033[m")
        sleep(3)
        continue
    if escolha == "2":
        while True:
            try:
                n1 = int(input("Digite o primeiro número: "))
            except ValueError:
                print("DIGITE APENAS NÚMEROS INTEIROS!")
                continue
            break
        while True:
            try:
                n2 = int(input("Digite o segundo número: "))
            except ValueError:
                print("DIGITE APENAS NÚMEROS INTEIROS!")
                continue
            break
        resultado = n1 - n2
        print(f"A subtração entre {n1} e {n2} é igual a \033[32m{resultado}\033[m")
        sleep(3)
        continue
    if escolha == "0":
        titulo("👋Até mais!")
        break
