import os 
os.system("cls" if os.name == "nt" else "clear")

while True:
    while True:
        try:
            entrada = input("Digite o valor da compra: R$").replace(",", ".").strip()
            compra = float(entrada)
        except ValueError:
            print("DIGITE APENAS NÚMEROS REAIS NESSA OPÇÃO!")
            continue
        break
    while True:
        escolha = input("Você quer continuar? [S/N] ").strip().upper()
        if escolha not in "SN" or escolha == "":
            print("Escolha apenas entre S (sim) ou N (não)!")
            continue
        break
    if escolha == "N":
        break
