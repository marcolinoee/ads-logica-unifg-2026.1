import os 
os.system("cls" if os.name == "nt" else "clear")

def formatação(foh):
    return f"R${foh:.2f}".replace(".", ",")

while True:
    try:    
        entrada = input("Digite o seu salário: R$").strip().replace(",", ".")
        salario = float(entrada)
    except ValueError:
        print("DIGITE APENAS NÚMEROS REIAS")
        continue
    break
if salario <= 1500.00:
    aumento = salario + (salario * 0.15)
    print(f"O seu aumento salárial foi de 15% e seu salário de {formatação(salario)} foi para {formatação(aumento)}")
elif 1500.00 < salario <= 3000.00:
    aumento = salario + (salario * 0.10)
    print(f"O seu aumento salárial foi de 10% e seu salário de {formatação(salario)} foi para {formatação(aumento)}")
else:
    aumento = salario + (salario * 0.05)
    print(f"O seu aumento salárial foi de 5% e seu salário de {formatação(salario)} foi para {formatação(aumento)}")
    