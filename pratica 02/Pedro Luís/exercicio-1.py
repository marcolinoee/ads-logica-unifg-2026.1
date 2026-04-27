import os 
os.system("cls" if os.name == "nt" else "clear")

while True:
    try:
        entrada = input("Digite um número: ").replace(",", ".").strip()
        saida = float(entrada)
    except ValueError:
        print("DIGITE APENAS NÚMEROS REAIS!")
        continue
    break
if saida > 0:
    print(f"O número {saida:.2f} é positivo.")
elif saida < 0:
    print(f"O número {saida:.2f} é negativo.")
else:
    print("O número é igual a zero!")